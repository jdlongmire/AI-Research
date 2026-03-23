---
layout: article
title: "The Frontier Is Closed – And That's a Problem for National Defense"
date: 2026-03-23
featured: true
featured_image: featured.png
description: "The U.S. Defense Industrial Base has cleared cloud access to frontier AI. But two structural gaps remain that no amount of IL authorization closes."
---

The U.S. Defense Industrial Base has access to frontier AI. More access than most people realize.

That's the good news. And it matters that we get it right before identifying where the problem actually is.

---

Over the past two years, the cleared cloud ecosystem has made genuine progress. Microsoft's Azure OpenAI Service is now DISA-authorized across all DoD impact levels: IL4 and IL5 for CUI, IL6 for Secret, and top secret work at the ICD503 level. AWS has followed a parallel path, with frontier models from Anthropic and Meta now approved in GovCloud regions, and a new Secret-West Region standing up to support classified AI workloads. The most recent Azure Government blog reports GPT-5.2 available in Secret and Top Secret cloud environments. AWS has committed $50 billion to new federal AI data centers specifically engineered for classified AI, breaking ground in 2026.

This is not nothing. Defense contractors and government agencies working CUI, Secret, and even some top secret workloads now have cloud-based access to genuine frontier capability. The policy and infrastructure investment to get here was substantial, and it's worth acknowledging.

But cleared cloud access and sovereign, self-hosted AI are not the same thing. And two structural gaps remain that no amount of IL authorization closes.

---

## The IP and Data Sovereignty Problem

Even inside a DISA-authorized cloud environment, the data governance picture is complicated. Prompts, query context, intermediate outputs, and the surrounding program information travel through infrastructure the contractor doesn't own. The provider operates it. The provider's personnel (cleared or otherwise) maintain it. The contractual protections are real, but they are not the same as having the model run entirely within your own boundary, on your own hardware, under your own administrative control.

For work involving export-controlled data, proprietary design information, competitive bid development, or early-stage program concepts, that distinction matters. A prime contractor developing a next-generation system doesn't want the context of that work (even sanitized fragments of it) anywhere outside a perimeter they control completely. The cleared cloud reduces exposure. Self-hosting eliminates it.

And self-hosting frontier capability isn't currently an option. The providers don't license their weights for self-deployment. The most capable models are API-only, by policy and by active lobbying for regulatory frameworks that would formalize that restriction. The contractor can access the frontier, but only on the provider's infrastructure, under the provider's terms.

---

## The Air Gap Problem

The second gap is harder, and it has two distinct faces that rarely get separated.

The first is on the development and delivery side. A significant class of defense programs (Special Access Programs, Compartmented Access Programs, compartmented SCI) operate under access controls that go well beyond classification level. These aren't just IL6 workloads. They're program-specific, often operating on networks with no external connectivity, or with one-way transfer controls that make cloud dependency structurally impossible regardless of how the cloud is authorized. For these programs, the cleared cloud isn't a solution: it's a category error. The work happens in environments that cannot reach any external endpoint, cleared or otherwise.

Engineers building AI-enabled capabilities for these programs face a mismatch. They can prototype against frontier capability in a cleared cloud environment. They cannot deliver that capability into the operational environment where it will actually run. The development environment and the operational environment are architecturally incompatible.

The second face is at the embedded solution level. An increasing class of defense requirements calls for AI that lives in the platform: in autonomous systems, edge devices, deployed ISR capabilities, weapons system support functions that operate disconnected from any network. These systems cannot phone home to an API. They need capable AI baked in and running locally. The open-weight models currently available for this purpose are capable, and closing the gap, but they remain meaningfully behind frontier in the reasoning and analytical tasks that matter most for demanding defense applications.

Both faces lead to the same place: the most capable AI is structurally unavailable for the most demanding defense use cases.

---

## The Safety Argument's Blind Spot

The providers' rationale for keeping weights closed is a mix of safety, liability, and competitive interest. The safety argument has some merit: if a frontier model has capabilities that could enable serious misuse, releasing weights removes the ability to constrain access. That's a coherent concern.

But the argument has a persistent blind spot. It treats every deployment context as equivalent. It doesn't account for cleared organizations operating inside controlled environments, under established security frameworks, building systems that are already among the most tightly governed in the country. The DIB isn't asking to post frontier weights on the open internet. It's asking to run them inside a CMMC-compliant enclave, on a SAP network with no external connectivity, or embedded in a classified platform: for work that is already surrounded by more access controls than most commercial software ever sees.

That use case gets no special treatment in the current licensing landscape. The same wall faces a defense prime working inside a SAP and a startup with no security posture at all.

---

## The Strategic Irony

There's a deeper strategic irony here. The U.S. has invested significantly in export controls, compute restrictions, and chip sanctions to prevent adversaries from developing frontier AI capability. The logic is sound: frontier AI is a strategic asset, and strategic assets shouldn't be handed to competitors.

But the export control regime protects American frontier capability from foreign adversaries while simultaneously making that capability inaccessible to the American defense sector's most demanding use cases. The strategic asset is being guarded at the border and withheld from the people who need it most.

China is not navigating a commercial licensing dispute with its frontier model developers. Qwen and DeepSeek are national strategic investments. The PLA doesn't file a support ticket when it needs on-premise, air-gapped deployment.

---

Two problems. One structural gap. And the policy conversation has mostly talked around both of them.

That needs to change.
