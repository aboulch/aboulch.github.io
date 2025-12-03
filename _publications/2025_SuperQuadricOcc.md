---
layout: publication
title: "SuperQuadricOcc: Multi-Layer Gaussian Approximation of Superquadrics for Real-Time Self-Supervised Occupancy Estimation"
author: "Seamie Hayes &ensp;
         Reenu Mohandas &ensp;
         Tim Brophy &ensp;
         Alexandre Boulch &ensp;
         Ganesh Sistu &ensp;
         Ciaran Eising
         "
permalink: /publications/2025_SuperQuadricOcc
date: 2025-11-20
venue: "arXiv"
---

[Arxiv](https://arxiv.org/abs/2511.17361){: .btn .btn-purple .mr-4 }
[Code](https://github.com/seamie6/SuperQuadricOcc){: .btn .btn-purple .mr-4 }

![SuperQuadricOcc teaser](/files/2025_SuperQuadricOcc/method.jpg)

### Abstract

<p align="justify">
Semantic occupancy estimation enables comprehensive scene understanding for automated driving, providing dense spatial and semantic information essential for perception and planning. While Gaussian representations have been widely adopted in self-supervised occupancy estimation, the deployment of a large number of Gaussian primitives drastically increases memory requirements and is not suitable for real-time inference. In contrast, superquadrics permit reduced primitive count and lower memory requirements due to their diverse shape set. However, implementation into a self-supervised occupancy model is nontrivial due to the absence of a superquadric rasterizer to enable model supervision. Our proposed method, SuperQuadricOcc, employs a superquadric-based scene representation. By leveraging a multi-layer icosphere-tessellated Gaussian approximation of superquadrics, we enable Gaussian rasterization for supervision during training. On the Occ3D dataset, SuperQuadricOcc achieves a 75% reduction in memory footprint, 124% faster inference, and a 5.9% improvement in mIoU compared to previous Gaussian-based methods, without the use of temporal labels. To our knowledge, this is the first occupancy model to enable real-time inference while maintaining competitive performance. The use of superquadrics reduces the number of primitives required for scene modeling by 84% relative to Gaussian-based approaches. Finally, evaluation against prior methods is facilitated by our fast superquadric voxelization module.
</p>

### Results

![SuperQuadricOcc results](/files/2025_SuperQuadricOcc/teaser.png)

### Citation


```
@article{hayes2025superquadricocc,
  title={SuperQuadricOcc: Multi-Layer Gaussian Approximation of Superquadrics for Real-Time Self-Supervised Occupancy Estimation},
  author={Hayes, Seamie and Mohandas, Reenu and Brophy, Tim and Boulch, Alexandre and Sistu, Ganesh and Eising, Ciaran},
  journal={arXiv preprint arXiv:2511.17361},
  year={2025}
}
```