---
title: "ShaResNet: reducing residual network parameter number by sharing weights"
collection: publications
permalink: /publication/2018-sharesnet
excerpt: ''
date: 2018-02-01
venue: 'Pattern Recognition Letters'
paperurl: ''
type: 'journal'
---

Author: *A. Boulch*

**Abstract**: Deep residual networks have reached the state of the art in many image processing tasks such image classification. However, the cost for a gain in accuracy in terms of depth and memory is prohibitive as it requires a higher number of residual blocks, up to double the initial value. To tackle this problem, we propose in this paper a way to reduce the redundant information of the networks. We share the weights of convolutional layers between residual blocks operating at the same spatial scale. The signal flows multiple times in the same convolutional layer. The resulting architecture, called ShaResNet, contains block specific layers and shared layers. These ShaResNet are trained exactly in the same fashion as the commonly used residual networks. We show, on the one hand, that they are almost as efficient as their sequential counterparts while involving less parameters, and on the other hand that they are more efficient than a residual network with the same number of parameters. For example, a 152-layer-deep residual network can be reduced to 106 convolutional layers, i.e. a parameter gain of 39%, while loosing less than 0.2% accuracy on ImageNet.


[Download paper here](https://arxiv.org/abs/1702.08782)

Code available at [Github](https://github.com/aboulch/sharesnet).

```
@article{BOULCH201853,
title = "Reducing parameter number in residual networks by sharing weights",
journal = "Pattern Recognition Letters",
volume = "103",
pages = "53 - 59",
year = "2018",
issn = "0167-8655",
doi = "https://doi.org/10.1016/j.patrec.2018.01.006",
url = "http://www.sciencedirect.com/science/article/pii/S0167865518300060",
author = "Alexandre Boulch"
}
```

The previous version was at Arxiv (Note that this is not the reviewed version).
Major modifications have been done since this version.

```
@article{DBLP:journals/corr/Boulch17,
  author    = {Alexandre Boulch},
  title     = {ShaResNet: reducing residual network parameter number by sharing weights},
  journal   = {CoRR},
  volume    = {abs/1702.08782},
  year      = {2017},
  url       = {http://arxiv.org/abs/1702.08782},
  archivePrefix = {arXiv},
  eprint    = {1702.08782},
  timestamp = {Wed, 07 Jun 2017 14:40:36 +0200},
  biburl    = {http://dblp.org/rec/bib/journals/corr/Boulch17},
  bibsource = {dblp computer science bibliography, http://dblp.org}
}
```
