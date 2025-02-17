---
layout: publication
title: "SALUDA: Surface-based Automotive Lidar Unsupervised Domain Adaptation"
author: "B. Michele, A. Boulch, G. Puy, T.-H. Vu, R. Marlet, N. Courty"
permalink: /publications/2024_3DV_saluda
date: 2024-03-18
venue: "International Conference on 3D vision (3DV)"
---

[Arxiv](https://arxiv.org/abs/2304.03251){: .btn .btn-purple .mr-4 }
[Code](https://github.com/valeoai/saluda){: .btn .btn-purple .mr-4 }

![SALUDA teaser](/images/publications/2024_3DV_saluda/teaser.png)

### Abstract

Learning models on one labeled dataset that generalize well on another domain is a difficult task, as several shifts might happen between the data domains. This is notably the case for lidar data, for which models can exhibit large performance discrepancies due for instance to different lidar patterns or changes in acquisition conditions. This paper addresses the corresponding Unsupervised Domain Adaptation (UDA) task for semantic segmentation. To mitigate this problem, we introduce an unsupervised auxiliary task of learning an implicit underlying surface representation simultaneously on source and target data. As both domains share the same latent representation, the model is forced to accommodate discrepancies between the two sources of data. This novel strategy differs from classical minimization of statistical divergences or lidar-specific domain adaptation techniques. Our experiments demonstrate that our method achieves a better performance than the current state of the art, both in real-to-real and synthetic-to-real scenarios.


### Citation


```
@article{michele2023saluda,
  title={SALUDA: Surface-based Automotive Lidar Unsupervised Domain Adaptation},
  author={Michele, Bjoern and Boulch, Alexandre and Puy, Gilles and Vu, Tuan-Hung and Marlet, Renaud and Courty, Nicolas},
  journal={arXiv preprint arXiv:2304.03251},
  year={2023}
}
```