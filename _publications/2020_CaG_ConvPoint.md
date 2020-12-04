---
title: "ConvPoint: Continuous Convolutions for Point Cloud Processing"
author: "A. Boulch"
collection: publications
permalink: 2020_cag_convpoint
date: 2020-01-01
type: journal
venue: "Computers & Graphics"
venue2: "Eurographics Workshop 3D Object Retrieval (3DOR) 2019"
venue3:
paperurl: "https://www.sciencedirect.com/science/article/abs/pii/S0097849320300224"
arxivurl: "https://arxiv.org/abs/1904.02375"
halurl: 
codeurl: "https://github.com/aboulch/ConvPoint"
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: "https://aboulch.github.io/files/talks/2019_3dor_conv_slides.pdf"
teaser: "/files/2020_cag_convpoint/2020_cag_convpoint_thumbnail.png"
note:
noteimportant: 
---	


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