---
layout: publication
title: "Train Till You Drop: Towards Stable and Robust Source-free Unsupervised 3D Domain Adaptation"
author: "Björn Michele &ensp;
        Alexandre Boulch &ensp;
        Tuan-Hung Vu &ensp;
        Gilles Puy &ensp;
        Renaud Marlet &ensp;
        Nicolas Courty"
permalink: /publications/2024_ECCV_TTYD
date: 2024-09-29
type: conference
venue: "European Conference on Computer Vision (ECCV)"
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

[Arxiv](https://www.arxiv.org/abs/2409.04409){: .btn }
[Code](https://github.com/valeoai/TTYD){: .btn }

### Abstract

We tackle the challenging problem of source-free unsupervised domain adaptation (SFUDA) for 3D semantic segmentation. It amounts to performing domain adaptation on an unlabeled target domain without any access to source data; the available information is a model trained to achieve good performance on the source domain. A common issue with existing SFUDA approaches is that performance degrades after some training time, which is a by product of an under-constrained and ill-posed problem. We discuss two strategies to alleviate this issue. First, we propose a sensible way to regularize the learning problem. Second, we introduce a novel criterion based on agreement with a reference model. It is used (1) to stop the training when appropriate and (2) as validator to select hyperparameters without any knowledge on the target domain. Our contributions are easy to implement and readily amenable for all SFUDA methods, ensuring stable improvements over all baselines. We validate our findings on various 3D lidar settings, achieving state-of-the-art performance.
