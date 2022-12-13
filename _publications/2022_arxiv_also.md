---
layout: publication
title: "ALSO: Automotive Lidar Self-supervision by Occupancy estimation"
author: "A. Boulch, C. Sautier, B. Michele, G. Puy and Renaud Marlet"
permalink: /publications/2022_arxiv_also
date: 2022-12-13
type: 
venue: "arxiv"
venue2: 
venue3:
paperurl: 
arxivurl: https://arxiv.org/abs/2212.05867
halurl: 
codeurl: https://github.com/valeoai/ALSO
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser:
note:
noteimportant: 
---


### Abstract

We propose a new self-supervised method for pre-training the backbone of deep perception models operating on point clouds. The core idea is to train the model on a pretext task which is the reconstruction of the surface on which the 3D points are sampled, and to use the underlying latent vectors as input to the perception head. The intuition is that if the network is able to reconstruct the scene surface, given only sparse input points, then it probably also captures some fragments of semantic information, that can be used to boost an actual perception task. This principle has a very simple formulation, which makes it both easy to implement and widely applicable to a large range of 3D sensors and deep networks performing semantic segmentation or object detection. In fact, it supports a single-stream pipeline, as opposed to most contrastive learning approaches, allowing training on limited resources. We conducted extensive experiments on various autonomous driving datasets, involving very different kinds of lidars, for both semantic segmentation and object detection. The results show the effectiveness of our method to learn useful representations without any annotation, compared to existing approaches. Code is available at [https://github.com/valeoai/ALSO](https://github.com/valeoai/ALSO)