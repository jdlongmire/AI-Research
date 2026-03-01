#!/usr/bin/env python3
"""
Article Scheduler for AI-Research GitHub Pages
Moves scheduled articles to docs/articles/ when publish_date arrives.
Sends email notification on publish.
"""

import os
import sys
import shutil
import smtplib
import re
from datetime import datetime, date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

# Configuration
SCHEDULER_DIR = Path(__file__).parent
SCHEDULED_DIR = SCHEDULER_DIR / "scheduled"
ARTICLES_DIR = SCHEDULER_DIR.parent / "docs" / "articles"
SITE_URL = "https://aithinkr.net"

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "thinxai.jdl@gmail.com"
SENDER_PASSWORD = "tvkm jcxd ckqx xsnj"
NOTIFY_EMAIL = "longmire.jd@gmail.com"


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    frontmatter = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            frontmatter[key] = value

    return frontmatter


def update_frontmatter(content: str, updates: dict) -> str:
    """Update frontmatter values and remove specified keys."""
    if not content.startswith("---"):
        return content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return content

    lines = parts[1].strip().split("\n")
    new_lines = []

    for line in lines:
        if ":" in line:
            key = line.split(":", 1)[0].strip()
            # Skip keys we want to remove
            if key in ["publish_date", "draft"]:
                continue
            # Update keys if specified
            if key in updates:
                new_lines.append(f"{key}: {updates[key]}")
                del updates[key]
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    # Add any remaining updates
    for key, value in updates.items():
        new_lines.append(f"{key}: {value}")

    return f"---\n{chr(10).join(new_lines)}\n---{parts[2]}"


def send_notification(title: str, slug: str, url: str) -> bool:
    """Send email notification when article publishes."""
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = NOTIFY_EMAIL
        msg["Subject"] = f"Article Published: {title}"

        body = f"""Your scheduled article has been published.

Title: {title}
URL: {url}

The article is now live on aithinkr.net.

- ThinxAI Scheduler
"""
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        return True
    except Exception as e:
        print(f"Failed to send notification: {e}")
        return False


def publish_article(article_path: Path) -> bool:
    """Move article to docs/articles/ and update frontmatter."""
    # Determine if it's a directory (with index.md) or single file
    if article_path.is_dir():
        index_file = article_path / "index.md"
        if not index_file.exists():
            print(f"No index.md in {article_path}")
            return False
        content = index_file.read_text()
        slug = article_path.name
    else:
        content = article_path.read_text()
        slug = article_path.stem

    frontmatter = parse_frontmatter(content)
    title = frontmatter.get("title", slug)

    # Create destination
    dest_dir = ARTICLES_DIR / slug
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Build permalink if not already present
    permalink = f"/articles/{slug}/"
    updates = {}
    if "permalink" not in frontmatter:
        updates["permalink"] = permalink

    if article_path.is_dir():
        # Copy all files from the directory
        for item in article_path.iterdir():
            if item.name == "index.md":
                # Update frontmatter (add permalink, remove publish_date/draft)
                updated_content = update_frontmatter(content, updates)
                (dest_dir / "index.md").write_text(updated_content)
            else:
                shutil.copy2(item, dest_dir / item.name)
        # Remove source directory
        shutil.rmtree(article_path)
    else:
        # Single file - update and move
        updated_content = update_frontmatter(content, updates)
        (dest_dir / "index.md").write_text(updated_content)
        article_path.unlink()

    # Build URL
    article_url = f"{SITE_URL}/articles/{slug}/"

    print(f"Published: {title}")
    print(f"URL: {article_url}")

    # Send notification
    send_notification(title, slug, article_url)

    return True


def check_and_publish():
    """Check all scheduled articles and publish those ready."""
    if not SCHEDULED_DIR.exists():
        print("No scheduled directory found")
        return 0

    today = date.today()
    published_count = 0

    # Check both directories and single .md files
    items = list(SCHEDULED_DIR.iterdir())

    for item in items:
        if item.name.startswith("."):
            continue

        # Get content
        if item.is_dir():
            index_file = item / "index.md"
            if not index_file.exists():
                continue
            content = index_file.read_text()
        elif item.suffix == ".md":
            content = item.read_text()
        else:
            continue

        frontmatter = parse_frontmatter(content)
        publish_date_str = frontmatter.get("publish_date")

        if not publish_date_str:
            print(f"Skipping {item.name}: no publish_date")
            continue

        try:
            publish_date = datetime.strptime(publish_date_str, "%Y-%m-%d").date()
        except ValueError:
            print(f"Skipping {item.name}: invalid date format {publish_date_str}")
            continue

        if publish_date <= today:
            print(f"Publishing {item.name} (scheduled for {publish_date})")
            if publish_article(item):
                published_count += 1
        else:
            print(f"Not yet: {item.name} (scheduled for {publish_date})")

    return published_count


def main():
    """Main entry point."""
    print(f"Article Scheduler - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Checking: {SCHEDULED_DIR}")
    print("-" * 50)

    count = check_and_publish()

    print("-" * 50)
    print(f"Published {count} article(s)")

    return 0 if count >= 0 else 1


if __name__ == "__main__":
    sys.exit(main())
