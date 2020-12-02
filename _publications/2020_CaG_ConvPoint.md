---
title: "ConvPoint: Continuous Convolutions for Point Cloud Processing"
author: "A. Boulch"
collection: publications
permalink: 2020_cag_convpoint
date: 2020-01-01
type: journal
venue: "Computers & Graphics"
venue2: 
venue3:
paperurl: "https://www.sciencedirect.com/science/article/abs/pii/S0097849320300224"
arxivurl: "https://arxiv.org/abs/1904.02375"
halurl: 
codeurl: "https://github.com/aboulch/ConvPoint"
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser: "2019-3DOR-conv.png"
note:
noteimportant: 
---								

### Authors

Alexandre Boulch

<p style="text-align:center">
    <a href="https://www.sciencedirect.com/science/article/abs/pii/S0097849320300224">
        <img src="/images/logo_paper.png" width="64" class="center" />
    </a>&nbsp;&nbsp;&nbsp;
    <a href="https://arxiv.org/abs/1904.02375">
        <img src="/images/logo_arxiv.png" width="64" class="center" />
    </a>&nbsp;&nbsp;&nbsp;
    <a href="https://github.com/aboulch/ConvPoint">
        <img src="/images/logo_github.png" width="64" class="center"/>
    </a>
</p>

### Abstract

Point clouds are unstructured and unordered data, as opposed to images. Thus, most machine learning approach developed for image cannot be directly transferred to point clouds. In this paper, we propose a generalization of discrete convolutional neural networks (CNNs) in order to deal with point clouds by replacing discrete kernels by continuous ones. This formulation is simple, allows arbitrary point cloud sizes and can easily be used for designing neural networks similarly to 2D CNNs. We present experimental results with various architectures, highlighting the flexibility of the proposed approach. We obtain competitive results compared to the state-of-the-art on shape classification, part segmentation and semantic segmentation for large-scale point clouds.


### Citation

```
@article{boulch2020convpoint,
  title={ConvPoint: Continuous convolutions for point cloud processing},
  author={Boulch, Alexandre},
  journal={Computers \& Graphics},
  year={2020},
  publisher={Elsevier}
}
```