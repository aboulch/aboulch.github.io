---
layout: publication
title: 'Statistical Criteria for Shape Fusion and Selection'
author: 'A. Boulch and R. Marlet'
permalink: /publications/2014_icpr_shapes
date: 2014-01-01
venue: 'International Conference on Pattern Recognition, ICPR'
---

[Paper](https://dl.acm.org/doi/abs/10.1109/ICPR.2014.171){: .btn .btn-purple .mr-4}
[PDF](/files/2014_icpr_fusion/2014_icpr_fusion_boulch.pdf){: .btn .btn-purple .mr-4}
[Code](https://github.com/aboulch/primitive_merging){: .btn .btn-purple .mr-4}

![](/files/2014_icpr_fusion/teaser.png)

### Abstract

Surface reconstruction from point clouds often relies on a primitive extraction step, that may be followed by a merging step because of a possible over-segmentation. We present two statistical criteria to decide whether or not two surfaces are to be considered as the same, and thus can be merged. They are based on the statistical tests of Kolmogorov-Smirnov and Mann-Whitney for comparing distributions. Moreover, computation time can be significantly cut down using a reduced sampling based on the Dvoretzky-Keifer-Wolfowitz inequality. The strength of our approach is that it relies in practice on a single intuitive parameter (homogeneous to a distance) and that it can be applied to any shape, including meshes, not just geometric primitives. It also enables the comparison of shapes of different kinds, providing a way to choose between different shape candidates. We show several applications of our method, experimenting geometric primitive (planeand cylinder) detection, selection and fusion, both on precise laser scans and noisy photogrammetric 3D data.