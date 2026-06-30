+++
title = "Reinforcement learning practices in healtcare applications"
description = "There are fundamentally 3 important practices to consider when applying reinforcement learning in healthcare settings."
date = 2025-10-21
updated = 2025-10-21
draft = false
aliases = ["/posts/reinforcement-learning-practices-in-healthcare/"]

[taxonomies]
categories = ["2025"]
tags = ["reinforcement learning","ai", "healthcare"]

[extra]
topic = "Reinforcement Learning"
lang = "en"
toc = true
comment = true
copy = false
outdate_alert = false
outdate_alert_days = 120
math = true
mermaid = false
featured = false
reaction = true
+++

This note reviews practical reinforcement learning use cases in healthcare and the constraints that matter in deployment. The challenge is that policy learning in clinical settings is high-stakes, partially observed, and often offline. I summarize where RL is promising and where reliability and safety dominate design choices.


In healthcare applications, artificial intelligence (AI) plays a crucial role in transforming patient care, diagnostics, and treatment planning to make healthcare more efficient and effective. However, if AI is used improperly, it may leads to worse outcomes rather than improved ones.

In the subset of AI, reinforcement learning (RL) has shown great promise in optimising sequential decision-making processes, which are common settings in healtcare industry. However, applying RL in healthcare settings requires careful consideration of several important practices to ensure a safety outcome. To illustrate the pitfalls of reinforcement learning, we consider the sepsis management, which remains wide uncertainty in the way clinicians make decisions. 

In the context of sepsis, a history may include a patient's vital signs, laboratory results, administered treatments, and other relevant clinical information over time. The actions could involve decisions such as administering fluids, vasopressors, or antibiotics at different time points. The rewards are typically defined based on patient outcomes, such as survival rates, length of hospital stay, or improvement in clinical scores. Note that defining ideal sepsis resuscitation strategies is challenging due to the complex and dynamic nature of the condition, as well as the variability in patient responses to treatments, therefore it is not straightforward to define short-term rewards for each action taken.

Here are three fundamental concerns when applying reinforcement learning in healthcare:

# Is the AI given access to all variables that infleunce decision making?

RL agent can only ook at the recorded data, however there are much more information and context that should be taken into consideration. Failing to consider all variables may result in esitmates that are confounded by spurious correlation.

For instance, severely sick septic patients may receive fluids earlier than healthier patients yet have worse outcomes, which is clearly because of them being sicker in the first place, not because of fluids worsen the outcomes. Therefore, it is important to considers of pissble confounding factors, which even more than what is required for standard prediction studies, as the sequential nature of the problem could possibly lead to confounding effects in both long term and short term.

# How big was that big data?

This is relatively straightfoward. For any AI training, its necessary to feed the model an adequate amount of useful information, so is RL model. Logically, for RL model to evaluate a new policy, it needs to find a long, continuous sequence of decisions in the historical data that matches its new policy. 

In clinical trials, the mismatches between new treatment policy against historical data, also known as off-policy evaluation, the effective sample size can become small. The mismatches grow with the number of decisions in a patient's history. For one sepsis study, a cohort of 3,855 patients yielded an effective sample size of only a few dozen. Therefore, instead of exploring new treatment approaches, observational data shall be used only to refining existing practices.

# Will the AI behave prospectively as intended?

One of the core elements in the feedback loop of every RL is rewards. However, if the design of reward function is not handled properly (e.g. error in formulation, data processing etc.), the momdel will eventually laed to poor decisions.

Often, an overly simple reward function may neglect the long-term effects. For instance, rewarding only blood pressure targets may result in agent that harms long-term benefit by dosing excessive vasopressors to patients. Additionally, the learned policy might decay after a period of time if there's changes in the treatment standards.

Therefore, it is neccessary to use interpretable machine learning to interrogate and assess whether learned policies will behave as intended in a prospective clinincal setting

# Conclusion

In the end, although RL offers such promising opportunities to optimising sequential treatments in medical industry, we shall be cautious in deploying into production and requires due diligence to safely realise its potential in revolutionalising this life-saving industry. 

{{ figure(src="/img/posts/guidelines_for_reinforcement_learning_in_healthcare.jpg", alt="Guidelines for Reinforcement Learning in Healthcare", caption="Guidelines for Reinforcement Learning in Healthcare") }}

In the end, I would like to express my gratitude to Omer Gottesman et al. for providing such practical viewpoint in standardising the application of reinforcement learning in clinical settings.

References:
- Gottesman, O., Johansson, F., Komorowski, M., Faisal, A., Sontag, D., Doshi-Velez, F., & Celi, L. A. (2019). Guidelines for reinforcement learning in healthcare. Nature Medicine, 25(1), 16–18. [https://doi.org/10.1038/s41591-018-0310-5](https://doi.org/10.1038/s41591-018-0310-5)