---
title: 'High Resolution Semantic Change Detection'
collection: publications
permalink: /publications/2018-arxiv-change
excerpt: ''
date: 2018-10-01
venue: 'Arxiv'
paperurl: ''
type: 'misc'
author : 'R. D. Daudt, B. Le Saux, A. Boulch, Y. Gousseau'
---

**Abstract**: Change detection is one of the main problems in remote sensing, and is essential to the accurate processing and understanding of the large scale Earth observation data available through programs such as Sentinel and Landsat. Most of the recently proposed change detection methods bring deep learning to this context, but openly available change detection datasets are still very scarce, which limits the methods that can be proposed and tested. In this paper we present the first large scale high resolution semantic change detection (HRSCD) dataset, which enables the usage of deep learning methods for semantic change detection. The dataset contains coregistered RGB image pairs, pixel-wise change information and land cover information. We then propose several methods using fully convolutional neural networks to perform semantic change detection. Most notably, we present a network architecture that performs change detection and land cover mapping simultaneously, while using the predicted land cover information to help to predict changes. We also describe a sequential training scheme that allows this network to be trained without setting a hyperparameter that balances different loss functions and achieves the best overall results. 


[Download paper here](https://arxiv.org/abs/1810.08452)

## Citation
```
@article{daudt2018high,
  title={High Resolution Semantic Change Detection},
  author={Daudt, Rodrigo Caye and Saux, Bertrand Le and Boulch, Alexandre and Gousseau, Yann},
  journal={arXiv preprint arXiv:1810.08452},
  year={2018}
}

```