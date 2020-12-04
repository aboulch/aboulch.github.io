---
title: "FKAConv: Feature-Kernel Alignment for Point Cloud Convolution"
author: "A. Boulch, G. Puy and R. Marlet"
collection: publications
permalink: 2020_accv_fkaconv
date: 2020-12-01
type: conference
venue: "15th Asian Conference on Computer Vision (ACCV 2020)"
venue2: 
venue3:
paperurl: "https://openaccess.thecvf.com/content/ACCV2020/html/Boulch_FKAConv_Feature-Kernel_Alignment_for_Point_Cloud_Convolution_ACCV_2020_paper.html"
arxivurl: "https://arxiv.org/abs/2004.04462"
halurl: 
codeurl: "https://github.com/valeoai/FKAConv"
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: "/files/2020_accv_fkaconv/2020_accv_fkaconv_slides.pdf"
teaser: "/files/2020_accv_fkaconv/2020_accv_fkaconv_thumbnail.png"
note:
noteimportant: 
---

### Abstract

Recent state-of-the-art methods for point cloud semantic segmentation are based on convolution defined for point clouds The interest goes beyond semantic segmentation. We propose a formulation of the convolution for point cloud directly inspired by the discrete convolution in image processing. The resulting formulation underlines the separation between the discrete kernel space and the geometric space where the points lies. Several existing methods fall under this formulation.The two spaces are linked with a space change matrix $\mathbf{A}$, estimated with a neural network. $\mathbf{A}$ softly assigns the input features on the convolution kernel. Finally, we show competitive results on several semantic segmentation benchmarks while being efficient both in computation time and memory.


### Citation

```
@inproceedings{boulch2020fkaconv,
  title={FKAConv: Feature-Kernel Alignment for Point Cloud Convolution},
  author={Boulch, Alexandre and Puy, Gilles and Marlet, Renaud},
  booktitle={Proceedings of the Asian Conference on Computer Vision},
  year={2020}
}
```