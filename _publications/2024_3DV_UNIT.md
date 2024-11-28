---
layout: publication
title: "UNIT: Unsupervised Online Instance Segmentation through Time"
author: "Corentin Sautier &ensp
        Gilles Puy &ensp
        Alexandre Boulch &ensp
        Renaud Marlet &ensp
        Vincent Lepetit"
permalink: /publications/2025_3DV_UNIT
date: 2025-03-25
type: conference
venue: "International Conference on 3D vision (3DV)"
paperurl: 
arxivurl:
halurl: 
codeurl: https://github.com/valeoai/UNIT
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser:
note:
noteimportant: 
---

[Arxiv](https://arxiv.org/abs/2409.07887){: .btn }
[Code](https://github.com/valeoai/UNIT){: .btn}

### Abstract

Online object segmentation and tracking in Lidar point clouds enables autonomous agents to understand their surroundings and make safe decisions. Unfortunately, manual annotations for these tasks are prohibitively costly. We tackle this problem with the task of class-agnostic unsupervised online instance segmentation and tracking. To that end, we leverage an instance segmentation backbone and propose a new training recipe that enables the online tracking of objects. Our network is trained on pseudo-labels, eliminating the need for manual annotations. We conduct an evaluation using metrics adapted for temporal instance segmentation. Computing these metrics requires temporally-consistent instance labels. When unavailable, we construct these labels using the available 3D bounding boxes and semantic labels in the dataset. We compare our method against strong baselines and demonstrate its superiority across two different outdoor Lidar datasets.

