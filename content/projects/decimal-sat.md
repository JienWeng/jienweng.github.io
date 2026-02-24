+++
title = "DecimalSat — 1U CubeSat Nanosatellite"
description = "A functional 1U CubeSat built with a multinational team. My work covered embedded C++ firmware for the OBC, ground station LoRa connectivity, and a fair amount of hands-on soldering."
date = 2025-06-01
draft = false

[taxonomies]
tags = ["C++", "Embedded Systems", "LoRa", "CubeSat", "Hardware", "Satellite"]

[extra]
lang = "en"
toc = false
comment = false
reaction = false
featured = true
img = "/img/projects/decimal-sat/assembled-sat.jpeg"
hero_img = ""
github = ""
demo = ""
status = "Completed"
period = "2024 – 2025"
video = ""
+++

Building a satellite that actually works feels different from what I expected. DecimalSat is a 1U CubeSat (10 x 10 x 10 cm), and most of the challenge is not physics but convincing four subsystems to trust each other enough to pass data reliably over LoRa. I came in as the embedded software developer and ended up touching more hardware than I planned. That tends to happen.

{{ figure(src="/img/projects/decimal-sat/assembled-sat.jpeg", alt="Assembled DecimalSat 1U CubeSat", caption="The finished satellite, all four subsystems stacked in the 1U frame.") }}

On the firmware side, I wrote the C++ code running on the OBC: packet framing, radio state machine, telemetry queuing. LoRa is forgiving over distance but not over bad configuration. Getting the spreading factor, bandwidth, and coding rate right without blowing the power budget took more iteration than expected.

On the ground station side, I built the software that receives packets, decodes telemetry frames, and makes them readable. Watching the first clean packet arrive is one of those moments you remember. The video below is that test.

{{ video(src="/img/projects/decimal-sat/lora-test.mp4", caption="LoRa link test, satellite transmitting and ground station receiving.") }}

{{ figure(src="/img/projects/decimal-sat/groundstation-module.jpeg", alt="Ground station LoRa receiver module", caption="The ground station receiver, the other end of the link.") }}

The hardware side was more hands-on than I expected. I did a fair amount of PCB soldering: SMD components on the EPS power board, through-hole connectors on antenna interfaces. At 1U scale there is no room to redo anything, which sharpens your attention considerably.

{{ figure(src="/img/projects/decimal-sat/soldering.jpeg", alt="Soldering PCB components", caption="Soldering on the EPS board.") }}

We built on top of a starter kit with pre-designed PCBs for the core subsystems, which meant we could focus on integration and firmware rather than schematic design from scratch. That was the right call for a project at this scope.

{{ figure(src="/img/projects/decimal-sat/starter-pack.jpeg", alt="Satellite module starter pack components", caption="The starter pack, our foundation before integration.") }}

Working across borders on something physical has its own set of challenges. You cannot push a fix and deploy, so things have to be in the same room eventually. We made it work through remote debugging, shared documentation, and a lot of patience across time zones. The team is what made it land.

{{ figure(src="/img/projects/decimal-sat/group.JPG", alt="The multinational DecimalSat team", caption="The team from multiple countries.") }}
