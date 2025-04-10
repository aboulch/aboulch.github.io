---
layout: publication
title: "FLOT: Scene Flow on Point Clouds Guided by Optimal Transport"
author: "G. Puy, A. Boulch and R. Marlet"
permalink: /publications/2020_eccv_flot
date: 2020-01-01
venue: "European Conference on Computer Vision (ECCV)"
---

[Paper](https://link.springer.com/chapter/10.1007/978-3-030-58604-1_32){: .btn .btn-purple .mr-4 }
[Arxiv](https://arxiv.org/abs/2007.11142){: .btn .btn-purple .mr-4 }

### Abstract

We propose and study a method called FLOT that estimates scene flow on point clouds. We start the design of FLOT by noticing that scene flow estimation on point clouds reduces to estimating a permutation matrix in a perfect world. Inspired by recent works on graph matching, we build a method to find these correspondences by borrowing tools from optimal transport. Then, we relax the transport constraints to take into account real-world imperfections. The transport cost between two points is given by the pairwise similarity between deep features extracted by a neural network trained under full supervision using synthetic datasets. Our main finding is that FLOT can perform as well as the best existing methods on synthetic and real-world datasets while requiring much less parameters and without using multiscale analysis. Our second finding is that, on the training datasets considered, most of the performance can be explained by the learned transport cost. This yields a simpler method, FLOT0, which is obtained using a particular choice of optimal transport parameters and performs nearly as well as FLOT.

### Citation

```
@InProceedings{10.1007/978-3-030-58604-1_32,
title="FLOT: Scene Flow on Point Clouds Guided by Optimal Transport",
author="Puy, Gilles and Boulch, Alexandre and Marlet, Renaud",
booktitle="Computer Vision -- ECCV 2020",
year="2020",
publisher="Springer International Publishing",
pages="527--544",
isbn="978-3-030-58604-1"
}
```

