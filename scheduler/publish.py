#!/usr/bin/env python3
"""
Article Scheduler for AI-Research GitHub Pages
Moves scheduled articles to docs/articles/ when publish_date arrives.
Generates featured images using Gemini, sends email notification on publish.
"""

import os
import sys
import shutil
import smtplib
import re
import uuid
from datetime import datetime, date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    from google import genai
    from google.genai import types
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Configuration
SCHEDULER_DIR = Path(__file__).parent
SCHEDULED_DIR = SCHEDULER_DIR / "scheduled"
ARTICLES_DIR = SCHEDULER_DIR.parent / "docs" / "articles"
SITE_URL = "https://aithinkr.net"

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "thinxai.jdl@gmail.com"
SENDER_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "tzxnuricxncoufzv")
NOTIFY_EMAIL = "longmire.jd@gmail.com"

# Image resizing configuration
MAX_IMAGE_WIDTH = 800
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp', '.gif'}

# Gemini image generation configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyD3WDLcoWA2Ip7Trg96hT_mdCmkZ-PKpIQ")
GEMINI_IMAGE_MODEL = "gemini-2.0-flash-exp-image-generation"


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


def resize_images(directory: Path) -> int:
    """Resize all images in directory to max width for mobile-friendliness."""
    if not PIL_AVAILABLE:
        print("  Warning: Pillow not installed, skipping image resize")
        return 0

    resized_count = 0
    for img_path in directory.iterdir():
        if img_path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        if img_path.suffix.lower() == '.gif':
            # Skip GIFs to preserve animation
            continue

        try:
            with Image.open(img_path) as img:
                if img.width > MAX_IMAGE_WIDTH:
                    # Calculate new height maintaining aspect ratio
                    ratio = MAX_IMAGE_WIDTH / img.width
                    new_height = int(img.height * ratio)

                    # Resize with high-quality resampling
                    resized = img.resize((MAX_IMAGE_WIDTH, new_height), Image.Resampling.LANCZOS)

                    # Save (convert RGBA to RGB for JPEG)
                    if img_path.suffix.lower() in {'.jpg', '.jpeg'} and resized.mode == 'RGBA':
                        resized = resized.convert('RGB')

                    resized.save(img_path, optimize=True, quality=85)
                    print(f"  Resized: {img_path.name} ({img.width}x{img.height} → {MAX_IMAGE_WIDTH}x{new_height})")
                    resized_count += 1
        except Exception as e:
            print(f"  Warning: Could not resize {img_path.name}: {e}")

    return resized_count


def make_images_responsive(content: str) -> str:
    """Add responsive CSS to image tags in markdown content."""
    # Pattern to find markdown images: ![alt](src)
    # Add responsive style if not already present
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'

    def replace_image(match):
        alt = match.group(1)
        src = match.group(2)
        # Return HTML img tag with responsive styling
        return f'<img src="{src}" alt="{alt}" style="max-width: 100%; height: auto;">'

    return re.sub(pattern, replace_image, content)


def generate_featured_image(title: str, description: str, output_dir: Path) -> str | None:
    """Generate a featured image using Gemini based on article title and description.

    Returns the filename if successful, None otherwise.
    """
    if not GEMINI_AVAILABLE:
        print("  Warning: google-genai not installed, skipping image generation")
        return None

    # Build a prompt for the featured image
    prompt = f"""Create a professional, visually striking featured image for a blog article.

Article title: {title}
Article topic: {description}

Style guidelines:
- Modern, clean design suitable for a tech/AI research blog
- Abstract or conceptual representation of the topic
- Professional color palette (blues, purples, teals work well)
- Avoid text in the image
- 16:9 aspect ratio for blog header

Generate an image that would work well as a blog post header/featured image."""

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        response = client.models.generate_content(
            model=GEMINI_IMAGE_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE'],
            ),
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                ext = 'png'
                if 'jpeg' in (part.inline_data.mime_type or ''):
                    ext = 'jpg'

                filename = f'featured.{ext}'
                filepath = output_dir / filename
                filepath.write_bytes(part.inline_data.data)

                print(f"  Generated featured image: {filename}")
                return filename

        print("  Warning: Gemini returned no image data")
        return None

    except Exception as e:
        print(f"  Warning: Failed to generate featured image: {e}")
        return None


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
    description = frontmatter.get("description", title)

    # Create destination
    dest_dir = ARTICLES_DIR / slug
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Generate featured image using Gemini
    print(f"  Generating featured image for: {title}")
    featured_filename = generate_featured_image(title, description, dest_dir)

    # Build permalink if not already present
    permalink = f"/articles/{slug}/"
    updates = {}
    if "permalink" not in frontmatter:
        updates["permalink"] = permalink

    # Add featured_image to frontmatter if generated
    if featured_filename:
        updates["featured_image"] = featured_filename

    if article_path.is_dir():
        # Copy all files from the directory
        for item in article_path.iterdir():
            if item.name == "index.md":
                # Update frontmatter and make images responsive
                updated_content = update_frontmatter(content, updates)
                updated_content = make_images_responsive(updated_content)
                (dest_dir / "index.md").write_text(updated_content)
            else:
                shutil.copy2(item, dest_dir / item.name)

        # Resize images for mobile-friendliness
        resize_images(dest_dir)

        # Remove source directory
        shutil.rmtree(article_path)
    else:
        # Single file - update, make images responsive, and move
        updated_content = update_frontmatter(content, updates)
        updated_content = make_images_responsive(updated_content)
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
