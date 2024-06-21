---
layout: publication
title: "Weakly Supervised Change Detection Using Guided Anisotropic Diffusion"
author: "R. C. Daudt, B. Le Saux, A. Boulch and Y. Gousseau"
permalink: /publications/2021_mlj_weak_change
date: 2021-04-01
type: journal
venue: "Machine Learning Journal"
paperurl: "https://link.springer.com/article/10.1007/s10994-021-06008-4"
arxivurl:
halurl: 
codeurl: 
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser: "/files/2019_cvprw_change_detection/2019_cvprw_change_detection_thumbnail.png"
note:
noteimportant: 
---


### Abstract

Large scale datasets created from crowdsourced labels or openly available data have become crucial to provide training data for large scale learning algorithms. While these datasets are easier to acquire, the data are frequently noisy and unreliable, which is motivating research on weakly supervised learning techniques. In this paper we propose original ideas that help us to leverage such datasets in the context of change detection. First, we propose the guided anisotropic diffusion (GAD) algorithm, which improves semantic segmentation results using the input images as guides to perform edge preserving filtering. We then show its potential in two weakly-supervised learning strategies tailored for change detection. The first strategy is an iterative learning method that  combines model optimisation and  data cleansing using GAD to extract the useful information from a large scale change detection dataset generated from open vector data. The second one incorporates GAD within a novel spatial attention layer that increases the accuracy of weakly supervised networks trained to perform pixel-level predictions from image-level labels. Improvements with respect to state-of-the-art are demonstrated on 4 different public datasets.

### Citation


```
@article{daudt2021weakly,
  title={Weakly supervised change detection using guided anisotropic diffusion},
  author={Daudt, Rodrigo Caye and Le Saux, Bertrand and Boulch, Alexandre and Gousseau, Yann},
  journal={Machine Learning},
  pages={1--27},
  year={2021},
  publisher={Springer}
}
```