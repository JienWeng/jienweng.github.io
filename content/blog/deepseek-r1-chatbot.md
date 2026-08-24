+++
title = "Making Deepseek R1 ChatBot"
description = "A chatbot built using Hugging Face's Deepseek R1 Distilled 1.5B model to enhance user interactions and provide intelligent responses."
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

I built a small chatbot with DeepSeek-R1 because I wanted to see how a local reasoning model behaved when its intermediate output was made visible. The useful parts were the setup decisions, the strange mistakes, and the few things I would change next time.

[![“Good artists copy, great artists steal” - Steve Jobs](https://cdn.cosmos.so/d66e7a6d-8205-4e9c-ba4f-656971c79857?format=jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:7291035071992520704/)

DeepSeek being open source was the main reason I wanted to try it. I did not need to wait for an API account or a company to decide how I could use the model. I could download it, tinker with it, and see what happened.

So I went ahead and built the chatbot I had wanted to make for a long time. It is not packed with fancy features yet, but the experiment gave me a better feel for how DeepSeek R1 behaves. You can try it out live [here](https://huggingface.co/spaces/jienweng/chatbot_v2).

The technical details are below.

### Showing the model's reasoning output

The part I found most surprising was separating the model’s reasoning output from its final response. In a conventional chatbot, the answer appears without the intermediate work. Here, the model produces a visible sequence of reasoning before the final response, so I could watch it break down a problem and revise its answer. I had not seen that behaviour in the other LLMs I had used.

At first, I didn’t plan for this feature. It appeared while I was testing different ways to improve response quality. I noticed that the model was generating hidden reasoning steps before its final output. Instead of discarding them, I decided to show them. The result made the AI feel more transparent, almost like it was thinking out loud.

[![Fun Fact: The "thinking" parts are actually generated as HTML!](https://cdn.cosmos.so/b65be583-5569-41e4-ab62-b4bf500120e1?format=jpeg)](https://huggingface.co/spaces/jienweng/chatbot_v2)

For example, if you ask it something like, “What do you think about climate change in Malaysia?”, you won’t just get a final answer out of nowhere. You’ll actually see the model go through a step-by-step breakdown of its thought process:

1. Breaking down the question components
2. Evaluating current knowledge
3. Forming logical connections
4. Combining the pieces into a response

The response was often structured. It analysed the question, split it into different angles, and then assembled an answer instead of jumping straight to a conclusion.

[![Interesting Observation: The model sometimes includes unexpected details, some accurate and some a bit off!](https://cdn.cosmos.so/6c9e3e2a-d318-4615-8786-7d60248fc049?format=jpeg)](https://huggingface.co/spaces/jienweng/chatbot_v2)

That said, while the response does sound solid, there are some oddities that make me wonder what’s going on under the hood. For example, it mentions “the subtropical Andaman and Nicobar Islands,” which, uh, aren’t even part of Malaysia. Also, “Ch bamboo” initiative? Never heard of that one. These small but noticeable mistakes show that while the model is good at structuring its answers, it still struggles with factual accuracy.

But that’s exactly what makes having a visible thought process so useful. Instead of just blindly trusting AI responses, we can now see how the model arrives at its conclusions, which means we can spot errors more easily. If it had **hallucinated** this stuff in a normal chatbot, I might not have even noticed. But because I can watch it reason through the problem, I can tell where things might be going wrong.

[![AI Hallucination Meme](https://cdn.cosmos.so/8cf44525-7111-4a09-87c7-ee6a09d3cb3b?format=jpeg)](https://huggingface.co/spaces/jienweng/chatbot_v2)

Seeing the intermediate output also made mistakes easier to catch. I could inspect the path to an answer, correct the prompt, and compare the next response instead of treating the final text as unexplained output.

### Deployment Specifications

The chatbot is currently hosted on Hugging Face Spaces, running on a basic-tier instance, which means it’s not exactly a powerhouse but still gets the job done. Here’s what it’s running on:

* CPU: 2 vCPUs
* RAM: 16GB
* Storage: Basic instance storage
* Framework: Gradio
* Inference Optimization: FP16 quantization
* Average Response Time: 2-3 seconds
* Concurrent Users Supported: Up to 10

You might notice that the [live preview](https://huggingface.co/spaces/jienweng/chatbot_v2) here can be a bit slow while generating responses. That’s because the hardware isn’t optimized for LLM inference, so it’s working with some limitations. Hope you can bear with it! 😆

### Efficient Model Architecture

The chatbot uses the DeepSeek R1 Distilled 1.5B model, a compressed version of the original 685B parameter model. Despite having only 1.5 billion parameters, it reports strong results on several reasoning tasks.

Key points about the model:

* Original model: [DeepSeek R1 (685B)](https://huggingface.co/deepseek-ai/DeepSeek-R1)
* Distilled version: [DeepSeek R1 Distill Qwen 1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)
* 440x parameter reduction while maintaining core capabilities

[![Model Architecture](https://cdn.cosmos.so/8eb746ad-784b-4892-9eb0-4cd26a82af13?format=jpeg)](https://huggingface.co/blog/open-r1)

### Benchmark results

The model holds up well against much larger models on several published benchmarks, although that does not make it the best choice for every task.

[![Model Comparison Results](https://cdn.cosmos.so/2ac19291-5c72-4a60-b290-bd140a61a4d4?format=jpeg)](https://medium.com/data-science-in-your-pocket/deepseek-r1-distill-qwen-1-5b-the-best-small-sized-llm-14eee304d94b)


#### Selected results

1. **AIME 2024 (Math Competition)**
   * DeepSeek R1 Distilled: 28.9% Pass\@1
   * GPT-4o: 9.3% Pass\@1
   * Claude 3.5: 16.0% Pass\@1
2. **MATH-500 (Mathematical Reasoning)**
   * DeepSeek R1 Distilled: 83.9% Pass\@1
   * GPT-4o: 74.6% Pass\@1
   * Claude 3.5: 78.3% Pass\@1
3. **Codeforces (Competitive Programming)**
   * DeepSeek R1 Distilled: 954 Rating
   * GPT-4o: 759 Rating
   * Claude 3.5: 717 Rating



### Model Strengths & Limitations

**Strengths:**

* Superior reasoning capabilities, especially in mathematics
* Highly efficient with only 1.5B parameters
* Effective knowledge distillation from larger models
* Excellent performance in zero-shot scenarios

**Limitations:**

* Lower performance in general coding tasks
* Potential language mixing issues
* Sensitivity to prompt formatting
* Limited performance in broader general knowledge tasks

This balanced perspective shows why I chose this model for my chatbot implementation - it provides exceptional reasoning capabilities while remaining lightweight enough for practical deployment.



### Try It Yourself

Due to iframe restrictions, you can access the live demo through these methods:

1. [Direct Link to Demo](https://huggingface.co/spaces/jienweng/chatbot_v2)
2. [Docker Spaces documentation](https://huggingface.co/docs/hub/spaces-sdks-docker)
3. [Source Code](https://huggingface.co/spaces/jienweng/chatbot_v2/tree/main)

[![Chatbot interface](https://cdn.cosmos.so/0eab3363-76da-4dab-b44b-a4a5d7cdc96f?format=jpeg)](https://huggingface.co/spaces/jienweng/chatbot_v2)

### What I learned

DeepSeek made it easier for me to experiment with a capable reasoning model without relying on a paid API. The open-source release also meant I could inspect the model card, run a local or hosted version, and change the interface around it.

My chatbot is still small and not feature-packed, but it gave me a practical way to study the model's reasoning output and its failure modes. You can try it out live [here](https://huggingface.co/spaces/jienweng/chatbot_v2).

### Additional Resources

* [Model Card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)
* [Deployment Guide](https://huggingface.co/docs/hub/spaces-overview)
* [Performance Benchmarks](https://huggingface.co/spaces/mteb/leaderboard)
* [Community Discussion](https://discuss.huggingface.co/)


### References

1. **DeepSeek R1 (685B)**\
   *The original DeepSeek R1 model, a large-scale AI model with 685 billion parameters, was the precursor to the distilled 1.5B version used in the chatbot.*\
   [Source](https://huggingface.co/deepseek-ai/DeepSeek-R1)
2. **DeepSeek R1 Distill Qwen 1.5B**\
   *This is the distilled version of the DeepSeek R1 model, compressed to 1.5 billion parameters while retaining core capabilities.*\
   [Source](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)
3. **Open R1 Model Architecture**\
   *Explore the detailed architecture of the DeepSeek R1 model, showcasing its design and structure.*\
   [Source](https://huggingface.co/blog/open-r1)
4. **Medium - Deepseek R1 Distill Qwen 1.5B Performance**\
   *A comparison of the performance between Deepseek R1 Distilled and other models, showing its impressive results in multiple domains.*\
   [Source](https://medium.com/data-science-in-your-pocket/deepseek-r1-distill-qwen-1-5b-the-best-small-sized-llm-14eee304d94b)
5. **Hugging Face Space - Chatbot Demo**\
   *Live demo of the Deepseek R1 chatbot that showcases the model’s response and reasoning capabilities.*\
   [Source](https://huggingface.co/spaces/jienweng/chatbot_v2)
6. **Hugging Face - API Documentation**\
   *Official API documentation for Hugging Face Spaces, helping developers interact with models and integrate them into applications.*\
   [Source](https://huggingface.co/docs/hub/spaces-sdks-docker)
7. **Hugging Face - Source Code**\
   *Direct access to the source code of the Deepseek R1 chatbot project on Hugging Face Spaces for those interested in contributing or learning.*\
   [Source](https://huggingface.co/spaces/jienweng/chatbot_v2/tree/main)
8. **Hugging Face - Model Card**\
   *Official card for the Deepseek R1 Distilled model, providing details on its functionality and training specifications.*\
   [Source](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)
9. **Hugging Face - Deployment Guide**\
   *Guidelines for deploying models and applications using Hugging Face Spaces.*\
   [Source](https://huggingface.co/docs/hub/spaces-overview)
10. **Hugging Face - Performance Benchmarks**\
    *An overview of the model performance across various tasks and benchmarks, showcasing the strengths and weaknesses of different models.*\
    [Source](https://huggingface.co/spaces/mteb/leaderboard)
11. **Hugging Face - Community Discussion**    
    *Join the community discussions on Hugging Face, where users can ask questions, share insights, and discuss AI-related topics.*\
    [Source](https://discuss.huggingface.co/)
