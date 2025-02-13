---
layout: publication
title: "POCO: Point Convolution for Surface Reconstruction"
author: "A. Boulch and R. Marlet"
permalink: /publications/2022_cvpr_poco
date: 2022-03-01
venue: "Computer Vision and Pattern Recognition (CVPR)"
---

[Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Boulch_POCO_Point_Convolution_for_Surface_Reconstruction_CVPR_2022_paper.html){: .btn }
[Arxiv](https://arxiv.org/abs/2201.01831){: .btn}
[Code](https://github.com/valeoai/POCO){: .btn }


### Abstract

Implicit neural networks have been successfully used for surface reconstruction from point clouds. However, many of them face scalability issues as they encode the isosurface function of a whole object or scene into a single latent vector. To overcome this limitation, a few approaches infer latent vectors on a coarse regular 3D grid or on 3D patches, and interpolate them to answer occupancy queries. In doing so, they loose the direct connection with the input points sampled on the surface of objects, and they attach information uniformly in space rather than where it matters the most, i.e., near the surface. Besides, relying on fixed patch sizes may require discretization tuning. To address these issues, we propose to use point cloud convolutions and compute latent vectors at each input point. We then perform a learning-based interpolation on nearest neighbors using inferred weights. Experiments on both object and scene datasets show that our approach significantly outperforms other methods on most classical metrics, producing finer details and better reconstructing thinner volumes.


### Citation


```
@article{boulch2022poco,
  title={POCO: Point Convolution for Surface Reconstruction},
  author={Boulch, Alexandre and Marlet, Renaud},
  journal={arXiv preprint arXiv:2201.01831},
  year={2022}
}
```