+++
title = "Building a DeepSeek-R1 Chatbot"
description = "A Gradio chatbot experiment with visible intermediate output and the 1.5B distilled DeepSeek-R1 model."
date = 2024-12-30
updated = 2024-12-30
draft = false
aliases = ["/posts/deepseek-r1-chatbot/"]

[taxonomies]
categories = ["2024"]
tags = ["AI"]

[extra]
lang = "en"
toc = true
comment = true
copy = false
outdate_alert = true
outdate_alert_days = 120
math = false
mermaid = false
featured = false
reaction = false
+++

I built a chatbot with DeepSeek-R1-Distill-Qwen-1.5B to try a downloadable reasoning model. The interface shows its intermediate output separately from the final response.

[Try the Hugging Face demo](https://huggingface.co/spaces/jienweng/chatbot_v2) or [read the source](https://huggingface.co/spaces/jienweng/chatbot_v2/tree/main).

## Showing the intermediate output

The model produced reasoning text before its answer, so I displayed it instead of discarding it.

{{ figure(src="https://cdn.cosmos.so/b65be583-5569-41e4-ab62-b4bf500120e1?format=jpeg", alt="Chatbot displaying intermediate model output above the response", caption="Intermediate output shown above the answer.") }}

Asked about climate change in Malaysia, it gave a structured response that included the Andaman and Nicobar Islands and a “Ch bamboo” initiative I had never heard of. It sounded convincing despite those mistakes.

{{ figure(src="https://cdn.cosmos.so/6c9e3e2a-d318-4615-8786-7d60248fc049?format=jpeg", alt="Climate response with incorrect references to Malaysian geography", caption="A climate answer with wrong Malaysian geography.") }}

The intermediate text helped me inspect responses and compare prompts. It still needed fact-checking.

## Hosting the experiment

I used Gradio on a basic Hugging Face Spaces instance with 2 vCPUs and 16 GB RAM, so the demo can be slow to respond.

The small model kept things manageable: I could download it, read the model card, and change the interface without a paid inference API.

{{ figure(src="https://cdn.cosmos.so/0eab3363-76da-4dab-b44b-a4a5d7cdc96f?format=jpeg", alt="Chatbot interface", caption="The chatbot interface.") }}

Model details and published results are on the [official model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B); hosting is in the [Spaces documentation](https://huggingface.co/docs/hub/spaces-overview).
