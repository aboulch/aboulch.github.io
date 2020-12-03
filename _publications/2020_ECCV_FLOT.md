---
title: "FLOT: Scene Flow on Point Clouds Guided by Optimal Transport"
author: "G. Puy, A. Boulch and R. Marlet"
collection: publications
permalink: 2020_eccv_flot
date: 2020-01-01
type: conference
venue: "European Conference on Computer Vision (ECCV)"
venue2: 
venue3:
paperurl: "https://link.springer.com/chapter/10.1007/978-3-030-58604-1_32"
arxivurl: "https://arxiv.org/abs/2007.11142"
halurl: 
codeurl: 
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser: "/files/2020_eccv_flot/2020_eccv_flot_thumbnail.png"
note:
noteimportant: 
---

<p style="text-align:center">
    <a href="https://link.springer.com/chapter/10.1007/978-3-030-58604-1_32"><img src="/images/logo_paper.png" width="64" class="center" /></a>&nbsp;&nbsp;&nbsp;
    <a href="https://arxiv.org/abs/2007.11142"><img src="/images/logo_arxiv.png" width="64" class="center" /></a>
</p>


### Authors

Gilles Puy, Alexandre Boulch and Renaud Marlet

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

