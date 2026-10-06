+++
title = "Monash Water Platform: Wastewater Monitoring & CitizenFlood"
description = "Explore the Monash Water Platform: CitizenFlood Android water reporting, a wastewater monitoring dashboard, and Jien Weng’s research work in Malaysia."
template = "project-detail.html"
updated = 2026-10-06
[extra]
project_id = "monash-water"
search_topics = ["wastewater monitoring", "CitizenFlood Android app", "water observations", "operator dashboard", "Monash University Malaysia", "wastewater treatment plant research"]
toc = true
+++

## Wastewater monitoring research at Monash University Malaysia

The Monash Water Platform is part of my research assistant work at Monash University Malaysia. It brings community water observations, wastewater monitoring, and research information into a shared platform.

My research work includes wastewater treatment plant prediction using RNNs, Transformers, and Markov chain methods on time-series sensor data. The platform provides an application context for reporting and monitoring alongside that research.

## My role and the design decisions

As a research assistant, I develop prediction models from wastewater treatment plant sensor data. The platform connects that research context with community reporting and operator monitoring.

The two interfaces serve different tasks: CitizenFlood makes field observations accessible on Android, while the operator dashboard provides a place to inspect readings and explore scenarios. Keeping these tasks separate also helps distinguish a community report from a laboratory measurement or model output.

## CitizenFlood Android app for water observations

CitizenFlood lets people record site observations through an Android application. The reporting screen offers rainfall, water level, temperature, and wastewater reporting options.

The [Android download page](https://monash-water-platform.vercel.app/download) provides the APK and installation information. Community reports are observations; they should be interpreted separately from laboratory measurements.

## Wastewater treatment plant operator dashboard

The [operator dashboard](https://monash-water-platform.vercel.app/dashboard) supports wastewater monitoring and scenario exploration. Laboratory readings, community observations, and illustrative model outputs have different meanings and should retain their source context.

Scenario outputs are illustrative rather than validated predictions. The public dashboard’s plant-data service was unavailable when the portfolio images were captured, so this page shows the public platform and the actual Android reporting screen.

## Available outputs and research limits

The public outputs are the platform website, CitizenFlood APK download, and operator dashboard. The screenshots show the published platform and Android reporting interface.

Validation remains essential before a model output can support an operational decision. No prediction-accuracy or deployment-impact figure is presented here without a verified evaluation. My current research and publication statuses are recorded in the CV and publications page.

## Wastewater research, publications, and experience

For my role and broader work, see my [CV](@/cv/_index.md) and [research publications](@/publications/_index.md). The [public Monash Water Platform](https://monash-water-platform.vercel.app/) provides the current application and research entry points.
