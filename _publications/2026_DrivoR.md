---
layout: publication
title: "Driving on Registers"
author: "Ellington Kirby* &ensp;
         Alexandre Boulch* &ensp;
         Yihong Xu* &ensp;
         Yuan Yin &ensp;
         Gilles Puy &ensp;
         Eloi Zablocki &ensp;
         Andrei Bursuc &ensp;
         Spyros Gidaris &ensp;
         Renaud Marlet &ensp;
         Florent Bartoccioni &ensp;
         Anh-Quan Cao &ensp;
         Nermin Samet &ensp;
         Tuan-Hung VU &ensp;
         Matthieu Cord &ensp;
         "
permalink: /publications/2026_DrivoR
date: 2026-06-03
venue: "Computer Vision and Pattern Recognition (CVPR)"
---
[Project](https://valeoai.github.io/driving-on-registers/){: .btn .btn-purple .mr-4 }
[arXiv](https://arxiv.org/abs/2601.05083){: .btn .btn-purple .mr-4 }
[Code](https://github.com/valeoai/DrivoR){: .btn .btn-purple .mr-4 }

![DrivoR architecture](/files/2026_DrivoR/architecture.gif)

### Abstract

We present DrivoR, a simple and efficient transformer-based architecture for end-to-end autonomous driving. Our approach builds on pretrained Vision Transformers (ViTs) and introduces camera-aware register tokens that compress multi-camera features into a compact scene representation, significantly reducing downstream computation without sacrificing accuracy. These tokens drive two lightweight transformer decoders that generate and then score candidate trajectories. The scoring decoder learns to mimic an oracle and predicts interpretable sub-scores representing aspects such as safety, comfort, and efficiency, enabling behavior-conditioned driving at inference. Despite its minimal design, DrivoR outperforms or matches strong contemporary baselines across NAVSIM-v1, NAVSIM-v2, and the photorealistic closed-loop HUGSIM benchmark. Our results show that a pure-transformer architecture, combined with targeted token compression, is sufficient for accurate, efficient, and adaptive end-to-end driving.

