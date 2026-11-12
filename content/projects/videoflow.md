+++
title = "VideoFlow: Canvas-Based AI Video Studio"
description = "A Go, SvelteKit, and Electron video studio connecting characters, scripts, scenes, text-to-image, image-to-video, and editing in a canvas workflow."
template = "project-detail.html"
updated = 2026-11-12
[extra]
project_id = "videoflow"
search_topics = ["AI video creation", "canvas workspace", "Go backend", "SvelteKit", "Electron desktop application", "text-to-image", "image-to-video", "video editing"]
toc = true
+++

## Studio workflow

I work on the Go backend, SvelteKit interface, and Electron packaging. VideoFlow connects scripts, characters, scenes, shots, and media jobs so generated assets stay attached to their references.

The canvas brings story elements and generated outputs into one workspace. Select a character, scene, or asset to edit its details or ask for AI-assisted changes. The workflow supports text-to-image and image-to-video generation, followed by video editing, captions, and composition work.

## Go and SvelteKit with an Electron desktop application

The frontend uses SvelteKit and the backend uses Go. Project data is stored locally with SQLite and media files.

The Electron application starts a private local backend and displays the same frontend in a desktop window. Desktop packages include the Go engine, FFmpeg, FFprobe, and fonts, so users do not need to install the development toolchain to run the application.

The web version uses the shared frontend and backend through Docker. It is a single-user deployment; the desktop interface and the web studio share the same underlying workflow.

## Local project storage and AI providers

Keeping project data and media together makes the workspace portable between sessions. Current source uses local Codex or Claude Code sessions for text planning, fal.ai for image/video generation, and OpenRouter for vision and transcription, with other supported media routes available in settings. Provider setup depends on the release; see the [current provider guide](https://github.com/JienWeng/videoflow-go/blob/main/docs/PROVIDERS.md).

AI services require the relevant account access and, for paid generation, provider credits. Local project storage does not make cloud generation offline. The built-in editor and optional HyperFrames composition workflow support further editing; the [editing guide](https://github.com/JienWeng/videoflow-go/blob/main/docs/LOCAL-DIRECTOR.md) describes the available controls and limitations.

## Recorded workflow

<p id="workflow-transcript">The 19-second recording shows a real local session: enter Maya’s name and description, create the character, visit the Scenes workspace, then open Studio and select Maya on the story canvas. The demo uses an isolated project and has no audio. It demonstrates character creation and navigation; AI generation and rendering are not shown.</p>

## VideoFlow source code and desktop downloads

Download the desktop application from [GitHub releases](https://github.com/JienWeng/videoflow-go/releases). The release notes describe available platforms and installation requirements.

The [VideoFlow repository](https://github.com/JienWeng/videoflow-go) contains the implementation, setup instructions, and desktop release information. The [desktop and web guide](https://github.com/JienWeng/videoflow-go/blob/main/docs/ELECTRON-AND-WEB.md) explains the shared architecture and packaging.

For related writing on managing machine-learning workflows, read my [introduction to MLOps](@/notes/intro-to-mlops-tutorial.md).
