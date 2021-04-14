---
title: "Semi-Supervised Semantic Segmentation in Earth Observation: The MiniFrance Suite, Dataset Analysis and Multi-task Network Study"
author: "J. Castillo-Navarro, B. Le Saux, A. Boulch, N. Audebert, and S. Lefèvre"
collection: publications
permalink: 2021_mlj_semisup
date: 2021-01-01
type: journal
venue: "accepted at Machine Learning Journal"
venue2: 
venue3:
paperurl: 
arxivurl: "https://arxiv.org/abs/2010.07830"
halurl: 
codeurl: 
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser: "/files/2020_ml_semisup/2020_ml_semisup_thumbnail.png"
note:
noteimportant: 
---

Accepted but not publisehd yet.

### Abstract

The development of semi-supervised learning techniques is essential to enhance the generalization capacities of machine learning algorithms. Indeed, raw image data are abundant while labels are scarce, therefore it is crucial to leverage unlabeled inputs to build better models. The availability of large databases have been key for the development of learning algorithms with high level performance.
Despite the major role of machine learning in Earth Observation to derive products such as land cover maps, datasets in the field are still limited, either because of modest surface coverage, lack of variety of scenes or restricted classes to identify. We introduce a novel large-scale dataset for semi-supervised semantic segmentation in Earth Observation, the MiniFrance suite. MiniFrance has several unprecedented properties: it is large-scale, containing over 2000 very high resolution aerial images, accounting for more than 200 billions samples (pixels); it is varied, covering 16 conurbations in France, with various climates, different landscapes, and urban as well as countryside scenes; and it is challenging, considering land use classes with high-level semantics. Nevertheless, the most distinctive quality of MiniFrance is being the only dataset in the field especially designed for semi-supervised learning: it contains labeled and unlabeled images in its training partition, which reproduces a life-like scenario. Along with this dataset, we present tools for data representativeness analysis in terms of appearance similarity and a thorough study of MiniFrance data, demonstrating that it is suitable for learning and generalizes well in a semi-supervised setting. Finally, we present semi-supervised deep architectures based on multi-task learning and the first experiments on MiniFrance.

### Citation

```
@article{castillo2020semi,
  title={Semi-Supervised Semantic Segmentation in Earth Observation: The MiniFrance Suite, Dataset Analysis and Multi-task Network Study},
  author={Castillo-Navarro, Javiera and Saux, Bertrand Le and Boulch, Alexandre and Audebert, Nicolas and Lef{\`e}vre, S{\'e}bastien},
  journal={arXiv preprint arXiv:2010.07830},
  year={2020}
}
```