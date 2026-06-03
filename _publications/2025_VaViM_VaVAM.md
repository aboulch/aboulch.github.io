---
layout: publication
title: "VaViM and VaVAM: Autonomous Driving through Video Generative Modeling"
author: "Florent Bartoccioni &ensp;
        Elias Ramzi &ensp;
        Victor Besnier &ensp;
        Shashanka Venkataramanan &ensp;
        Tuan-Hung Vu &ensp;
        Yihong Xu &ensp;
        Loick Chambon &ensp;
        Spyros Gidaris &ensp;
        Serkan Odabas &ensp;
        David Hurych &ensp;
        Renaud Marlet &ensp;
        Alexandre Boulch &ensp;
        Mickael Chen &ensp;
        Éloi Zablocki &ensp;
        Andrei Bursuc &ensp;
        Eduardo Valle &ensp;
        Matthieu Cord"
permalink: /publications/2025_VaViM_VaVAM
date: 2025-02-01
venue: "Arxiv"
---

[Arxiv](https://arxiv.org/abs/2502.15672){: .btn .btn-purple .mr-4 }
[Code](https://github.com/valeoai/VideoActionModel){: .btn .btn-purple .mr-4 }
[Project](https://valeoai.github.io/vavim-vavam/){: .btn .btn-purple .mr-4 }

![VaViM VaVAM teaser](/files/2025_VaViM_VaVAM/teaser.jpg)

### Abstract

We explore the potential of large-scale generative video models for autonomous driving, introducing an open-source auto-regressive video model (VaViM) and its companion video-action model (VaVAM) to investigate how video pre-training transfers to real-world driving. VaViM is a simple auto-regressive video model that predicts frames using spatio-temporal token sequences. We show that it captures the semantics and dynamics of driving scenes. VaVAM, the video-action model, leverages the learned representations of VaViM to generate driving trajectories through imitation learning. Together, the models form a complete perception-to-action pipeline. We evaluate our models in open- and closed-loop driving scenarios, revealing that video-based pre-training holds promise for autonomous driving. Key insights include the semantic richness of the learned representations, the benefits of scaling for video synthesis, and the complex relationship between model size, data, and safety metrics in closed-loop evaluations.