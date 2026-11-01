+++
title = "VideoFlow: AI Video Orchestration with Go & Electron"
description = "Explore VideoFlow, an AI video orchestration platform built with Go, SvelteKit, and Electron for scripts, storyboards, render jobs, and local media workflows."
template = "project-detail.html"
updated = 2026-10-06
[extra]
project_id = "videoflow"
search_topics = ["AI video orchestration", "Go backend", "SvelteKit", "Electron desktop application", "FFmpeg", "storyboard workflow"]
toc = true
+++

## Studio workflow

I work on the Go backend, SvelteKit interface, and Electron packaging. VideoFlow connects scripts, characters, scenes, shots, and media jobs so generated assets stay attached to their references.

## Go and SvelteKit with an Electron desktop application

The frontend uses SvelteKit and the backend uses Go. Project data is stored locally with SQLite and media files.

The Electron application starts a private local backend and displays the same frontend in a desktop window. Desktop packages include the Go engine, FFmpeg, FFprobe, and fonts, so users do not need to install the development toolchain to run the application.

The web version uses the shared frontend and backend through Docker. It is a single-user deployment; the desktop interface and the web studio share the same underlying workflow.

## SQLite project storage and OpenRouter AI generation

Keeping project data and media together makes the workspace portable between sessions. AI generation still requires internet access and an OpenRouter API key with credits. Local storage does not make the generation service offline.

## Recorded workflow

<p id="workflow-transcript">The 19-second recording shows a real local session: enter Maya’s name and description, create the character, visit the Scenes workspace, then open Studio and select Maya on the story canvas. The demo uses an isolated project and has no audio. It demonstrates character creation and navigation; AI generation and rendering are not shown.</p>

## VideoFlow source code and desktop downloads

Download the desktop application from [GitHub releases](https://github.com/JienWeng/videoflow-go/releases). The release notes describe available platforms and installation requirements.

The [VideoFlow repository](https://github.com/JienWeng/videoflow-go) contains the implementation, setup instructions, and desktop release information. The [desktop and web guide](https://github.com/JienWeng/videoflow-go/blob/main/docs/ELECTRON-AND-WEB.md) explains the shared architecture and packaging.

For related writing on managing machine-learning workflows, read my [introduction to MLOps](@/notes/intro-to-mlops-tutorial.md).
