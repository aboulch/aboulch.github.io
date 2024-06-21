---
layout: publication
title: 'Statistical Criteria for Shape Fusion and Selection'
author: 'A. Boulch and R. Marlet'
permalink: /publications/2014_icpr_shapes
date: 2014-01-01
type: conference
venue: 'International Conference on Pattern Recognition, ICPR'
paperurl: 'https://dl.acm.org/doi/abs/10.1109/ICPR.2014.171'
arxivurl: 
halurl:
codeurl: 'https://github.com/aboulch/primitive_merging'
mediumurl: 
blogurl: 
pdfurl: /files/2014_icpr_fusion_boulch.pdf
slidesurl: 
teaser: /files/2014_icpr_fusion.png
note:
noteimportant:
---

![](/files/2014_icpr_fusion.png)

### Abstract

Surface reconstruction from point clouds often relies on a primitive extraction step, that may be followed by a merging step because of a possible over-segmentation. We present two statistical criteria to decide whether or not two surfaces are to be considered as the same, and thus can be merged. They are based on the statistical tests of Kolmogorov-Smirnov and MannWhitney for comparing distributions. Moreover, computation time can be significantly cut down using a reduced sampling based on the Dvoretzky-Keifer-Wolfowitz inequality. The strength of our approach is that it relies in practice on a single intuitive parameter (homogeneous to a distance) and that it can be applied to any shape, including meshes, not just geometric primitives. It also enables the comparison of shapes of different kinds, providing a way to choose between different shape candidates. We show several applications of our method, experimenting geometric primitive (planeand cylinder) detection, selection and fusion, both on precise laser scans and noisy photogrammetric 3D data.