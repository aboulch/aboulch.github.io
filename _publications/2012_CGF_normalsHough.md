---
layout: publication
title: "Fast Normal Estimation for Point Clouds with Sharp Features using a Robust Randomized Hough Transform"
author: "A. Boulch and R. Marlet"
permalink: /publications/2012_cgf_normals
date: 2012-01-01
venue: 'Computer Graphics Forum, Wiley'
venue2: 'Symposium on Geometry Processing 2012 (SGP 2012)'
venue3:
paperurl: 'https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-8659.2012.03181.x'
arxivurl: 
halurl: 
codeurl: 'https://github.com/aboulch/normals_Hough'
mediumurl: 
blogurl: 
pdfurl: /files/2012_cgf_normals_boulch.pdf
slidesurl: /files/2012_cgf_normals_slides_boulch.pdf
teaser: /files/2012_cgf_normals.png
thumbnail: /files/2012_cgf_normals.png
note:
noteimportant:
---

![](/files/2012_cgf_normals.png)

### Abstract

This paper presents a new method for estimating normals on unorganized point clouds that preserves sharp features. It is based on a robust version of the Randomized Hough Transform (RHT). We consider the filled Hough transform accumulator as an image of the discrete probability distribution of possible normals. The normals we estimate corresponds to the maximum of this distribution. We use a fixed-size accumulator for speed, statistical exploration bounds for robustness, and randomized accumulators to prevent discretization effects. We also propose various sampling strategies to deal with anisotropy, as produced by laser scans due to differences of incidence. Our experiments show that our approach offers an ideal compromise between precision, speed, and robustness:
it is at least as precise and noise-resistant as state-of-the-art methods that preserve sharp features, while being almost an order of magnitude faster. Besides, it can handle anisotropy with minor speed and precision losses