---
layout: publication
title: 'Piecewise‐planar 3D reconstruction with edge and corner regularization'
author: 'A. Boulch, M. De La Gorce and R. Marlet'
permalink: /publications/2014_cgf_reconstruction
date: 2014-01-01
venue: 'Computer Graphics Forum, Wiley <br/>
        Symposium on Geometry Processing 2014 (SGP 2014)'
---

[Paper](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.12431){: .btn .btn-purple .mr-4}
[PDF](/files/2014_cgf_reconstruction/2014_cgf_reconstruction_boulch.pdf){: .btn .btn-purple .mr-4}

![](/files/2014_cgf_reconstruction/2014_cgf_reconstruction.png)

### Abstract

This paper presents a method for the 3D reconstruction of a piecewise-planar surface from range images, typically laser scans with millions of points. The reconstructed surface is a watertight polygonal mesh that conforms
to observations at a given scale in the visible planar parts of the scene, and that is plausible in hidden parts. We
formulate surface reconstruction as a discrete optimization problem based on detected and hypothesized planes.
One of our major contributions, besides a treatment of data anisotropy and novel surface hypotheses, is a regularization of the reconstructed surface w.r.t. the length of edges and the number of corners. Compared to classical
area-based regularization, it better captures surface complexity and is therefore better suited for man-made environments, such as buildings. To handle the underlying higher-order potentials, that are problematic for MRF
optimizers, we formulate minimization as a sparse mixed-integer linear programming problem and obtain an approximate solution using a simple relaxation. Experiments show that it is fast and reaches near-optimal solutions.

### Citation

```
@inproceedings{boulch2014piecewise,
  title={Piecewise-planar 3D reconstruction with edge and corner regularization},
  author={Boulch, Alexandre and de La Gorce, Martin and Marlet, Renaud},
  booktitle={Computer Graphics Forum},
  volume={33},
  number={5},
  pages={55--64},
  year={2014},
  organization={Wiley Online Library}
}
```