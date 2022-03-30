---
layout: publication
title: "STaRFlow: A SpatioTemporal Recurrent Cell for Lightweight Multi-Frame Optical Flow Estimation"
author: "P.Godet, A. Boulch, A. Plyer and G. Le Besnerais"
permalink: /publications/2020_icpr_starflow
date: 2020-01-01
type: conference
venue: "25th international conference on pattern recognition (ICPR 2020)"
venue2: 
venue3:
paperurl: 
arxivurl: "https://arxiv.org/abs/2007.05481"
halurl: 
codeurl: "https://github.com/pgodet/star_flow"
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser: "/files/2020_icpr_starflow/2020_icpr_starflow_thumbnail.png"
note:
noteimportant: 
---



### Abstract

We present a new lightweight CNN-based algorithm for multi-frame optical flow estimation. Our solution introduces a double recurrence over spatial scale and time through repeated use of a generic "STaR" (SpatioTemporal Recurrent) cell. It includes (i) a temporal recurrence based on conveying learned features rather than optical flow estimates; (ii) an occlusion detection process which is coupled with optical flow estimation and therefore uses a very limited number of extra parameters. The resulting STaRFlow algorithm gives state-of-the-art performances on MPI Sintel and Kitti2015 and involves significantly less parameters than all other methods with comparable results.


### Citation

```
@article{godet2020starflow,
  title={STaRFlow: A SpatioTemporal Recurrent Cell for Lightweight Multi-Frame Optical Flow Estimation},
  author={Godet, Pierre and Boulch, Alexandre and Plyer, Aur{\'e}lien and Besnerais, Guy Le},
  journal={arXiv preprint arXiv:2007.05481},
  year={2020}
}
```