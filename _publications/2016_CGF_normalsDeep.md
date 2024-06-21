---
layout: publication
title: 'Deep Learning for Robust Normal Estimation in Unstructured Point Clouds'
author: 'A. Boulch and R. Marlet'
permalink: /publications/2016_cgf_normals
date: 2016-01-01
type: journal
venue: 'Computer Graphics Forum, Wiley <br/>
        Symposium on Geometry Processing 201 (SGP 2016)'
paperurl: 'https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.12983'
arxivurl: 
halurl: 
codeurl: 'https://github.com/aboulch/normals_HoughCNN'
mediumurl: 
blogurl: 
pdfurl: /files/2016_cgf_normals.pdf
slidesurl: /files/2016_cgf_normals_slides.pdf
teaser: '/files/2016-CGF-normals.png'
note:
noteimportant:
---

![](/files/2016_cgf_normals.png)

### Abstract

Normal estimation in point clouds is a crucial first step for numerous algorithms, from surface reconstruction and scene understanding to rendering. A recurrent issue when estimating normals is to make appropriate decisions close to sharp features, not to smooth edges, or when the sampling density is not uniform, to prevent bias. Rather than resorting to manually-designed geometric priors, we propose to learn how to make these decisions, using ground-truth data made from synthetic scenes. For this, we project a discretized Hough space representing normal directions onto a structure amenable to deep learning. The resulting normal estimation method outperforms most of the time the state of the art regarding robustness to outliers, to noise and to point density variation, in the presence of sharp edges, while remaining fast, scaling up to millions of points.