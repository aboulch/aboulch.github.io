---
layout: publication
title: "PCAM: Product of Cross-Attention Matrices for Rigid Registration of Point Clouds"
author: "A.-Q. Cao, G. Puy, A. Boulch and R. Marlet"
permalink: /publications/2021_iccv_pcam
date: 2021-10-11
type: conference
venue: "International Conference on Computer Vision (ICCV)"
paperurl:
arxivurl: "https://arxiv.org/abs/2110.01269"
halurl: 
codeurl: "https://github.com/valeoai/PCAM"
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser: "/files/2021_iccv_pcam/2021_iccv_pcam_thumbnail.png"
note:
noteimportant: 
---


### Abstract

Rigid registration of point clouds with partial overlaps is a longstanding problem usually solved in two steps: (a) finding correspondences between the point clouds; (b) filtering these correspondences to keep only the most reliable ones to estimate the transformation. Recently, several deep nets have been proposed to solve these steps jointly. We built upon these works and propose PCAM: a neural network whose key element is a pointwise product of cross-attention matrices that permits to mix both low-level geometric and high-level contextual information to find point correspondences. A second key element is the exchange of information between the point clouds at each layer, allowing the network to exploit context information from both point clouds to find the best matching point within the overlapping regions. The experiments show that PCAM achieves state-of-the-art results among methods which, like us, solve steps (a) and (b) jointly via deepnets.


### Citation

```
@inproceedings{cao21pcam,
  title={ {PCAM}: {P}roduct of {C}ross-{A}ttention {M}atrices for {R}igid {R}egistration of {P}oint {C}louds},
  author={Cao, Anh-Quan and Puy, Gilles and Boulch, Alexandre and Marlet, Renaud},
  booktitle={International Conference on Computer Vision (ICCV)},
  year={2021},
}
```