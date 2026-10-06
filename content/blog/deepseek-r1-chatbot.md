+++
title = "Building a DeepSeek-R1 Chatbot"
description = "A Gradio chatbot experiment with visible intermediate output and the 1.5B distilled DeepSeek-R1 model."
date = 2024-12-30
updated = 2024-12-30
draft = false
aliases = ["/posts/deepseek-r1-chatbot/"]

[taxonomies]
categories = ["2024"]
tags = ["ai"]

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

I built a chatbot with DeepSeek-R1-Distill-Qwen-1.5B to experiment with a downloadable reasoning model. The interface separates its intermediate output from the final response.

[Try the Hugging Face demo](https://huggingface.co/spaces/jienweng/chatbot_v2) or [read the source](https://huggingface.co/spaces/jienweng/chatbot_v2/tree/main).

## Showing the intermediate output

While testing responses, I noticed the model produced reasoning text before its answer. I decided to display it rather than discard it.

[![Chatbot displaying intermediate model output above the response](https://cdn.cosmos.so/b65be583-5569-41e4-ab62-b4bf500120e1?format=jpeg)](https://huggingface.co/spaces/jienweng/chatbot_v2)

Asked about climate change in Malaysia, it produced a structured response but included the Andaman and Nicobar Islands and a “Ch bamboo” initiative I had never heard of. The output sounded convincing despite those mistakes.

[![Climate response with incorrect references to Malaysian geography](https://cdn.cosmos.so/6c9e3e2a-d318-4615-8786-7d60248fc049?format=jpeg)](https://huggingface.co/spaces/jienweng/chatbot_v2)

Showing the intermediate text helped me inspect the response and compare prompts. It still needed fact-checking.

## Hosting the experiment

I used Gradio on a basic Hugging Face Spaces instance with 2 vCPUs and 16 GB RAM. That limits inference speed; the demo can take time to respond.

The small model made the experiment manageable. I could download it, inspect the model card, and change the interface without depending on a paid inference API.

[![Chatbot interface](https://cdn.cosmos.so/0eab3363-76da-4dab-b44b-a4a5d7cdc96f?format=jpeg)](https://huggingface.co/spaces/jienweng/chatbot_v2)

For model details and published results, see the [official model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B). The [Spaces documentation](https://huggingface.co/docs/hub/spaces-overview) covers hosting.
