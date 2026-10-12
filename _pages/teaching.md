---
layout: page
permalink: /teaching/
title: teaching
description: Course material for MSIA - Point clouds.
nav: true
nav_order: 4
---

## MSIA - Point clouds

### Evaluation

Choose a paper and a time slot [here](https://docs.google.com/spreadsheets/d/1xyd0vpf2dMOysuWdJ3U6bDxitowzhoWawHMgpoQT55g/edit?usp=sharing). A visio link will be added in the dedicated column.

**Rules of the game**: the idea is to do a presentation in the style of a conference presentation.

- 15 minutes slot
- 7 minutes presentation of the paper with slides (better not be overtime)
- 8 minutes discussion / questions on the paper and related notions

> **Warning - Colab notebooks**
> Copy / paste the link of the notebook (GitHub link) in Colab.
> Click on **Copy to Drive**, otherwise you cannot save the changes to the notebook.
{: .block-warning }

### Courses

#### From local properties to surface reconstruction

- Local features: normal estimation, normal orientation
- Surface reconstruction: ball pivoting, Delaunay reconstruction, Poisson reconstruction, RANSAC

[Slides]({{ '/assets/pdf/teaching/msia_point_clouds/MSIA_Points_3_surfaces.pdf' | relative_url }}){: .btn .btn-sm z-depth-0 }
[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_3_surfaces.ipynb){: .btn .btn-sm z-depth-0 }
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_3_surfaces_answers.ipynb){: .btn .btn-sm z-depth-0 }

#### Descriptors and classic ML

- Local descriptors
- Global descriptors
- Clustering

[Slides]({{ '/assets/pdf/teaching/msia_point_clouds/MSIA_Points_4_ML1.pdf' | relative_url }}){: .btn .btn-sm z-depth-0 }
[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_4_ML1.ipynb){: .btn .btn-sm z-depth-0 }
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_4_ML1_answers.ipynb){: .btn .btn-sm z-depth-0 }

#### Images and graph

- Image-based approaches
- Graph-based approaches

For the practical session, if not working on Google Colab directly, the material can be found on huggingface:

```python
from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="Msun/modelnet40", filename="modelnet40_ply_hdf5_2048.zip", repo_type="dataset", cache_dir=".")
!unzip ./datasets--Msun--modelnet40/snapshots/d5dc795541800feeb7a4b3bd3142729a0d2adf7a/modelnet40_ply_hdf5_2048
```

[Slides]({{ '/assets/pdf/teaching/msia_point_clouds/MSIA_Points_5_ML2.pdf' | relative_url }}){: .btn .btn-sm z-depth-0 }
[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_5_Geometric_Deep_Learning.ipynb){: .btn .btn-sm z-depth-0 }
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_5_Geometric_Deep_Learning_answers.ipynb){: .btn .btn-sm z-depth-0 }

#### From convolutions to transformers

- Convolutions on points
- Voxels
- Mixers and transformers

For the practical session, if not working on Google Colab directly, the material can be found on huggingface:

```python
from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="wangps/shapenet_segmentation", filename="shapenetcore_partanno_segmentation_benchmark_v0_normal.zip", repo_type="dataset", cache_dir=".")
!unzip -qq ./datasets--wangps--shapenet_segmentation/snapshots/dbde146b974e1fc8628b47b1b1c4e50d8bc1a2ef/shapenetcore_partanno_segmentation_benchmark_v0_normal
!mv shapenetcore_partanno_segmentation_benchmark_v0_normal shape_data
```

[Slides]({{ '/assets/pdf/teaching/msia_point_clouds/MSIA_Points_6_ML3.pdf' | relative_url }}){: .btn .btn-sm z-depth-0 }
[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_6_segmentation.ipynb){: .btn .btn-sm z-depth-0 }
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_6_segmentation_answers.ipynb){: .btn .btn-sm z-depth-0 }

#### Applications

- Tasks
- Self-supervised training
- Domain adaptation
- Open vocabulary

```python
import os
if not os.path.exists("./driving.hdf5"):
    !wget https://github.com/aboulch/MSIA_points/releases/download/v0.0.0/driving.tar.gz
    !tar -xvzf driving.tar.gz
```

[Slides]({{ '/assets/pdf/teaching/msia_point_clouds/MSIA_Points_7_ML4.pdf' | relative_url }}){: .btn .btn-sm z-depth-0 }
[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_7_maskclip.ipynb){: .btn .btn-sm z-depth-0 }
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_7_maskclip_answers.ipynb){: .btn .btn-sm z-depth-0 }

#### Geometric vision

- Structure from motion
- Neural Radiance Fields (NeRFs)
- Gaussian splatting
- Dust3R and follow-ups

[Slides]({{ '/assets/pdf/teaching/msia_point_clouds/MSIA_Points_8_rendering_multiview.pdf' | relative_url }}){: .btn .btn-sm z-depth-0 }
[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_8_ShapeRepresentation.ipynb){: .btn .btn-sm z-depth-0 }
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_8_ShapeRepresentation_answers.ipynb){: .btn .btn-sm z-depth-0 }
