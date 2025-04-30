---
layout: publication
title: "LiDPM: Rethinking Point Diffusion for Lidar Scene Completion"
author: "
        Tetiana Martyniuk &ensp;
        Gilles Puy &ensp;
        Alexandre Boulch &ensp;
        Renaud Marlet &ensp;
        Raoul de Charette
        "
permalink: /publications/2025_LiDPM
date: 2025-06-22
venue: "IEEE Intelligent Vehicles Symposium (IV 2025)"
---

[Arxiv](https://arxiv.org/abs/2504.17791){: .btn .btn-purple .mr-4 }
[Project](https://astra-vision.github.io/LiDPM/){: .btn .btn-purple .mr-4 }


![LiDPM teaser](/files/2025_LiDPM/teaser.png)

### Abstract

Training diffusion models that work directly on lidar points at the scale of outdoor scenes is challenging due to the difficulty of generating fine-grained details from white noise over a broad field of view. The latest works addressing scene completion with diffusion models tackle this problem by reformulating the original DDPM as a local diffusion process. It contrasts with the common practice of operating at the object level where vanilla DDPMs are used.

In this work, we close the gap between these two lines of work. We identify approximations in the local diffusion formulation, show that they are not required to operate at the scene level, and that a vanilla DDPM with a well-chosen starting point is enough for completion. Finally, we demonstrate that our method, LiDPM, leads to better results in scene completion on SemanticKITTI.