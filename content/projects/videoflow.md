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

## My work on VideoFlow

I work on the studio across the Go backend, SvelteKit interface, and Electron packaging. The project brings script planning, characters, scenes, shots, and media jobs into one workspace, with a shared interface for desktop and web use.

The central design problem is keeping the relationships between these stages visible. A generated image or video is useful only when it remains connected to the character, scene, or shot it belongs to.

## AI video orchestration: scripts, scenes, and storyboards

VideoFlow is an AI video orchestration platform that organises video work around a script, its characters, scenes, and individual shots. The studio makes those relationships visible so references and generation stages can be managed together.

The workflow moves from scripts and scene planning to storyboards, render jobs, and output assets. Character references, captions, and editing tools sit alongside that workflow. Generation and rendering produce outputs that can be inspected and worked on further.

## Go and SvelteKit with an Electron desktop application

The frontend uses SvelteKit and the backend uses Go. Project data is stored locally with SQLite and media files.

The Electron application starts a private local backend and displays the same frontend in a desktop window. Desktop packages include the Go engine, FFmpeg, FFprobe, and fonts, so users do not need to install the development toolchain to run the application.

The web version uses the shared frontend and backend through Docker. It is a single-user deployment; the desktop interface and the web studio share the same underlying workflow.

## SQLite project storage and OpenRouter AI generation

Keeping project data and media together makes the workspace portable between sessions. AI generation still requires internet access and an OpenRouter API key with credits. Local storage does not make the generation service offline.

## Recorded workflow

<p id="workflow-transcript">The 19-second recording shows a real local session: enter Maya’s name and description, create the character, visit the Scenes workspace, then open Studio and select Maya on the story canvas. The demo uses an isolated project and has no audio. It demonstrates character creation and navigation; AI generation and rendering are not shown.</p>

## What the project delivers

The public repository provides a working studio, local project storage, web deployment instructions, and desktop download information. The desktop packaging brings the engine and media tools together so users can start without installing the development toolchain.

The project is still evolving, with the current implementation focused on shared studio workflows and portable local projects.

## VideoFlow source code and desktop downloads

The [VideoFlow repository](https://github.com/JienWeng/videoflow-go) contains the implementation, setup instructions, and desktop release information. The [desktop and web guide](https://github.com/JienWeng/videoflow-go/blob/main/docs/ELECTRON-AND-WEB.md) explains the shared architecture and packaging.

For related writing on managing machine-learning workflows, read my [introduction to MLOps](@/notes/intro-to-mlops-tutorial.md).
