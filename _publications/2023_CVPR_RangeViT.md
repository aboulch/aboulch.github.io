---
layout: publication
title: "RangeViT: Towards Vision Transformers for 3D Semantic Segmentation in Autonomous Driving"
author: "A. Ando, S. Gidaris, A. Bursuc, G. Puy, A. Boulch, R. Marlet"
permalink: /publications/2023_cvpr_rangevit
date: 2023-01-01
type: conference
venue: "Computer Vision and Pattern Recognition (CVPR)"
venue2: 
venue3:
paperurl: "https://openaccess.thecvf.com/content/CVPR2023/html/Ando_RangeViT_Towards_Vision_Transformers_for_3D_Semantic_Segmentation_in_Autonomous_CVPR_2023_paper.html"
arxivurl: "https://arxiv.org/abs/2301.10222"
halurl: 
codeurl: "https://github.com/valeoai/rangevit"
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser:
note:
noteimportant: 
---

### Abstract

Casting semantic segmentation of outdoor LiDAR point clouds as a 2D problem, e.g., via range projection, is an effective and popular approach. These projection-based methods usually benefit from fast computations and, when combined with techniques which use other point cloud representations, achieve state-of-the-art results. Today, projection-based methods leverage 2D CNNs but recent advances in computer vision show that vision transformers (ViTs) have achieved state-of-the-art results in many image-based benchmarks. In this work, we question if projection-based methods for 3D semantic segmentation can benefit from these latest improvements on ViTs. We answer positively but only after combining them with three key ingredients: (a) ViTs are notoriously hard to train and require a lot of training data to learn powerful representations. By preserving the same backbone architecture as for RGB images, we can exploit the knowledge from long training on large image collections that are much cheaper to acquire and annotate than point clouds. We reach our best results with pre-trained ViTs on large image datasets. (b) We compensate ViTs' lack of inductive bias by substituting a tailored convolutional stem for the classical linear embedding layer. (c) We refine pixel-wise predictions with a convolutional decoder and a skip connection from the convolutional stem to combine low-level but fine-grained features of the the convolutional stem with the high-level but coarse predictions of the ViT encoder. With these ingredients, we show that our method, called RangeViT, outperforms existing projection-based methods on nuScenes and SemanticKITTI. 


### Citation


```
@article{ando2023rangevit,
  title={RangeViT: Towards Vision Transformers for 3D Semantic Segmentation in Autonomous Driving},
  author={Ando, Angelika and Gidaris, Spyros and Bursuc, Andrei and Puy, Gilles and Boulch, Alexandre and Marlet, Renaud},
  journal={arXiv preprint arXiv:2301.10222},
  year={2023}
}
```