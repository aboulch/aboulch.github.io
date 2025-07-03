---
layout: publication
title: "GaussRender: Learning 3D Occupancy with Gaussian Rendering"
author: "Loick Chambon &ensp;
        Eloi Zablocki &ensp;
        Alexandre Boulch &ensp;
        Mickael Chen &ensp;
        Matthieu Cord"
permalink: /publications/2025_GaussRender
date: 2025-10-19
venue: "International Conference on Computer Vision (ICCV)"
---

[Arxiv](https://arxiv.org/abs/2502.05040){: .btn .btn-purple .mr-4 }
[Code](https://github.com/valeoai/GaussRender){: .btn .btn-purple .mr-4 }

### Abstract

Understanding the 3D geometry and semantics of driving scenes is critical for developing of safe autonomous vehicles. While 3D occupancy models are typically trained using voxel-based supervision with standard losses (e.g., cross-entropy, Lovasz, dice), these approaches treat voxel predictions independently, neglecting their spatial relationships. In this paper, we propose GaussRender, a plug-and-play 3D-to-2D reprojection loss that enhances voxel-based supervision. Our method projects 3D voxel representations into arbitrary 2D perspectives and leverages Gaussian splatting as an efficient, differentiable rendering proxy of voxels, introducing spatial dependencies across projected elements. This approach improves semantic and geometric consistency, handles occlusions more efficiently, and requires no architectural modifications. Extensive experiments on multiple benchmarks (SurroundOcc-nuScenes, Occ3D-nuScenes, SSCBench-KITTI360) demonstrate consistent performance gains across various 3D occupancy models (TPVFormer, SurroundOcc, Symphonies), highlighting the robustness and versatility of our framework.
