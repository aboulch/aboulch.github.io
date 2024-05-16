---
layout: publication
title: "OccFeat: Self-supervised Occupancy Feature Prediction for Pretraining BEV Segmentation Networks"
author: "S. Sirko-Galouchenko, A. Boulch, S. Gidaris, A. Bursuc, A. Vobecky, P. Pérez, R. Marlet"
permalink: /publications/2024_WAD_OccFeat
date: 2024-06-17
type: conference
venue: "CVPR Workshop on Autonomous Driving (WAD)"
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

[Arxiv](https://arxiv.org/abs/2404.14027){: .btn }

![OccFeat teaser](/images/publications/2024_CVPR_WAD_OccFeat/teaser.png)

### Abstract

We introduce a self-supervised pretraining method, called OcFeat, for camera-only Bird's-Eye-View (BEV) segmentation networks. With OccFeat, we pretrain a BEV network via occupancy prediction and feature distillation tasks. Occupancy prediction provides a 3D geometric understanding of the scene to the model. However, the geometry learned is class-agnostic. Hence, we add semantic information to the model in the 3D space through distillation from a self-supervised pretrained image foundation model. Models pretrained with our method exhibit improved BEV semantic segmentation performance, particularly in low-data scenarios. Moreover, empirical results affirm the efficacy of integrating feature distillation with 3D occupancy prediction in our pretraining approach.


### Citation


```
@article{sirko2024occfeat,
  title={OccFeat: Self-supervised Occupancy Feature Prediction for Pretraining BEV Segmentation Networks},
  author={Sirko-Galouchenko, Sophia and Boulch, Alexandre and Gidaris, Spyros and Bursuc, Andrei and Vobecky, Antonin and P{\'e}rez, Patrick and Marlet, Renaud},
  journal={arXiv preprint arXiv:2404.14027},
  year={2024}
}
```