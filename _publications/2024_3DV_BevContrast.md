---
layout: publication
title: "BEVContrast: Self-Supervision in BEV Space for Automotive Lidar Point Clouds"
author: "C. Sautier, G. Puy, A. Boulch, R. Marlet, V. Lepetit"
permalink: /publications/2024_3DV_bevcontrast
date: 2024-03-18
type: conference
venue: "International Conference on 3D vision (3DV)"
venue2: 
venue3:
paperurl: 
arxivurl:
halurl: 
codeurl: 
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser:
note:
noteimportant: 
---

[Arxiv](https://arxiv.org/abs/2310.17281){: .btn }
[Code](https://github.com/valeoai/BEVContrast){: .btn}


![BEVContrast teaser](/images/publications/2024_3DV_bevcontrast/teaser.png)


### Abstract

We present a surprisingly simple and efficient method for self-supervision of 3D backbone on automotive Lidar point clouds. We design a contrastive loss between features of Lidar scans captured in the same scene. Several such approaches have been proposed in the literature from PointConstrast, which uses a contrast at the level of points, to the state-of-the-art TARL, which uses a contrast at the level of segments, roughly corresponding to objects. While the former enjoys a great simplicity of implementation, it is surpassed by the latter, which however requires a costly pre-processing. In BEVContrast, we define our contrast at the level of 2D cells in the Bird's Eye View plane. Resulting cell-level representations offer a good trade-off between the point-level representations exploited in PointContrast and segment-level representations exploited in TARL: we retain the simplicity of PointContrast (cell representations are cheap to compute) while surpassing the performance of TARL in downstream semantic segmentation.


### Citation


```
@article{sautier2023bevcontrast,
  title={BEVContrast: Self-Supervision in BEV Space for Automotive Lidar Point Clouds},
  author={Sautier, Corentin and Puy, Gilles and Boulch, Alexandre and Marlet, Renaud and Lepetit, Vincent},
  journal={arXiv preprint arXiv:2310.17281},
  year={2023}
}
```