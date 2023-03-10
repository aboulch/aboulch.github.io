---
layout: publication
title: "Using a Waffle Iron for Automotive Point Cloud Semantic Segmentation"
author: "G. Puy, A. Boulch, R. Marlet"
permalink: /publications/2023_arxiv_waffleiron
date: 2023-01-01
type: misc
venue: "Arxiv"
venue2: 
venue3:
paperurl: 
arxivurl: "https://arxiv.org/abs/2301.10100"
halurl: 
codeurl: "https://github.com/valeoai/WaffleIron"
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser:
note:
noteimportant: 
---

### Abstract

Semantic segmentation of point clouds in autonomous driving datasets requires techniques that can process large numbers of points over large field of views. Today, most deep networks designed for this task exploit 3D sparse convolutions to reduce memory and computational loads. The best methods then further exploit specificities of rotating lidar sampling patterns to further improve the performance, e.g., cylindrical voxels, or range images (for feature fusion from multiple point cloud representations). In contrast, we show that one can build a well-performing point-based backbone free of these specialized tools. This backbone, WaffleIron, relies heavily on generic MLPs and dense 2D convolutions, making it easy to implement, and contains just a few parameters easy to tune. Despite its simplicity, our experiments on SemanticKITTI and nuScenes show that WaffleIron competes with the best methods designed specifically for these autonomous driving datasets. Hence, WaffleIron is a strong, easy-to-implement, baseline for semantic segmentation of sparse outdoor point clouds.


### Citation


```
@article{puy2023waffleiron,
  title={Using a Waffle Iron for Automotive Point Cloud Semantic Segmentation},
  author={Puy, Gilles and Boulch, Alexandre and Marlet, Renaud},
  journal={arXiv preprint arXiv:2301.10100},
  year={2023}
}
```