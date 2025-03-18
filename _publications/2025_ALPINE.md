---
layout: publication
title: "Clustering is back: Reaching state-of-the-art LiDAR instance segmentation without training"
author: "
        Corentin Sautier &ensp;
        Gilles Puy &ensp;
        Alexandre Boulch &ensp;
        Renaud Marlet &ensp;
        Vincent Lepetit"
permalink: /publications/2025_ALPINE
date: 2025-03-18
venue: "Arxiv"
---

[Arxiv](https://arxiv.org/abs/2503.13203){: .btn .btn-purple .mr-4 }
[Code](https://github.com/valeoai/Alpine/){: .btn .btn-purple .mr-4 }


![ALPINE teaser](/files/2025_ALPINE/teaser.png)

### Abstract

Panoptic segmentation of LiDAR point clouds is fundamental to outdoor scene understanding, with autonomous driving being a primary application. While state-of-the-art approaches typically rely on end-to-end deep learning architectures and extensive manual annotations of instances, the significant cost and time investment required for labeling large-scale point cloud datasets remains a major bottleneck in this field. In this work, we demonstrate that competitive panoptic segmentation can be achieved using only semantic labels, with instances predicted without any training or annotations. Our method achieves performance comparable to current state-of-the-art supervised methods on standard benchmarks including SemanticKITTI and nuScenes, and outperforms every publicly available method on SemanticKITTI as a drop-in instance head replacement, while running in real-time on a single-threaded CPU and requiring no instance labels. Our method is fully explainable, and requires no learning or parameter tuning. Code is available at [this https URL](https://github.com/valeoai/Alpine/).
