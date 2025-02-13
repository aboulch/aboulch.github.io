---
layout: publication
title: "NeeDrop: Unsupervised Shape Representation from Sparse Point Clouds using Needle Dropping"
author: "A. Boulch, P.-A. Langlois, Gilles Puy and R. Marlet"
permalink: /publications/2021_3dv_needrop
date: 2021-12-01
venue: "International Conference on 3D vision (3DV)"
---

[Paper](https://www.computer.org/csdl/proceedings-article/3dv/2021/268800a940/1zWEezCujxC){: .btn }
[Arxiv](https://arxiv.org/abs/2111.15207){: .btn }
[Code](https://github.com/valeoai/NeeDrop){: .btn }


### Abstract

There has been recently a growing interest for implicit shape representations, with applications including surface reconstruction and generation. Contrary to explicit representations, they have no resolution limitations and they easily deal with a wide variety of surface topologies. To learn these implicit representations, current approaches rely on a certain level of shape supervision (e.g., inside/outside information or distance-to-shape knowledge), or at least require a dense point cloud (to approximate well enough the distance-to-shape). In contrast, we introduce NeeDrop, an unsupervised method for learning shape representations from possibly extremely sparse point clouds. Like in Buffon's needle problem, we ``drop'' (sample) needles on the point cloud and consider that, statistically, close to the surface, the needle end points lie on opposite sides of the surface. No shape knowledge is required and the point cloud can be highly sparse, e.g., as lidar point clouds acquired by vehicles. Previous unsupervised shape representation approaches fail to produce good-quality results on this kind of data. We obtain quantitative results on par with existing supervised approaches on shape reconstruction datasets and show promising qualitative results on hard autonomous driving datasets such as KITTI.