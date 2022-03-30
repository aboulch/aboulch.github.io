---
layout: publication
title: "POCO: Point Convolution for Surface Reconstruction"
author: "A. Boulch and R. Marlet"
permalink: /publications/2022_cvpr_poco
date: 2022-03-01
type: conference
venue: "Accepted at Computer Vision and Pattern Recognition (CVPR)"
venue2: 
venue3:
paperurl: 
arxivurl: https://arxiv.org/abs/2201.01831
halurl: 
codeurl: "https://github.com/valeoai/POCO"
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser:
note:
noteimportant: 
---

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