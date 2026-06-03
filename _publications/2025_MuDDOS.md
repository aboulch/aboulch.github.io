---
layout: publication
title: "Improving Multimodal Distillation for 3D Semantic Segmentation under Domain Shift"
author: "Björn Michele &ensp;
         Alexandre Boulch &ensp;
         Gilles Puy &ensp;
         Tuan-Hung Vu &ensp;
         Renaud Marlet &ensp;
         Nicolas Courty"
permalink: /publications/2025_BMVC_MuDDOS
date: 2025-11-24
venue: "British Machine Vision Conference (BMVC)"
---

[Paper](https://bmvc2025.bmva.org/proceedings/859/){: .btn .btn-purple .mr-4 }
[Arxiv](https://arxiv.org/abs/2511.17455){: .btn .btn-purple .mr-4 }
[Code](https://github.com/valeoai/muddos){: .btn .btn-purple .mr-4 }
[Poster](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_859/poster.pdf){: .btn .btn-purple .mr-4 }

![MuDDOS teaser](/files/2025_MuDDOS/teaser.png)

### Abstract

Semantic segmentation networks trained under full supervision for one type of lidar fail to generalize to unseen lidars without intervention. To reduce the performance gap under domain shifts, a recent trend is to leverage vision foundation models (VFMs) providing robust features across domains. In this work, we conduct an exhaustive study to identify recipes for exploiting VFMs in unsupervised domain adaptation for semantic segmentation of lidar point clouds. Building upon unsupervised image-to-lidar knowledge distillation, our study reveals that: (1) the architecture of the lidar backbone is key to maximize the generalization performance on a target domain; (2) it is possible to pretrain a single backbone once and for all, and use it to address many domain shifts; (3) best results are obtained by keeping the pretrained backbone frozen and training an MLP head for semantic segmentation. The resulting pipeline achieves state-of-the-art results in four widely-recognized and challenging settings.

### Citation


```
@inproceedings{michele2025muddos,
  title={Improving Multimodal Distillation for 3D Semantic Segmentation under Domain Shift},
  author={Michele, Bj{\"o}rn and Boulch, Alexandre and  Vu, Tuan-Hung and Puy, Gilles and Marlet, Renaud and Courty, Nicolas},
  booktitle={Proceedings of the British Machine Vision Conference (BMVC)},
  year={2025}
}
```