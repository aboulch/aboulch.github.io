---
layout: default
title: Teaching
nav_order: 6
permalink: /teaching/
---

# MSIA - Point clouds

## Evaluation:

Chose a paper and time slot here:
[LINK](https://docs.google.com/spreadsheets/d/1xyd0vpf2dMOysuWdJ3U6bDxitowzhoWawHMgpoQT55g/edit?usp=sharing)
A visio link will be added in the dedicated column.

#### Rules of the game
The idea is to do presentation in the style of a conference presentation.
* 15 minutes slot
* 7 minutes presentation of the paper with slides (better not be overtime)
* 8 minutes discussion / questions on the paper and related notions.





{: .warning }
> **Colab notebooks**
> 
> Copy / paste the link of the notebook (github link) in colab
>
> Click on **Copy to Drive** oterwise you cannot save the changes to the notebook


## From local properties to surface reconstruction

* Local features
  * Normal estimation
  * Normal orientation
* Surface reconstruction
  * Ball pivoting
  * Delaunay reconstruction
  * Poisson reconstruction
  * RANSAC

[Slides](/files/course/msia_point_clouds/MSIA_Points_3_surfaces.pdf){: .btn .btn-purple .mr-4}

#### Practical session

[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_3_surfaces.ipynb){: .btn .btn-purple .mr-4 }
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_3_surfaces_answers.ipynb){: .btn .btn-purple .mr-4 }


## Descriptors and classic ML

* Descriptors
  * Local descriptors
  * Global descriptors
  * Clustering

[Slides](/files/course/msia_point_clouds/MSIA_Points_4_ML1.pdf){: .btn .btn-purple .mr-4}

### Practical session

[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_4_ML1.ipynb){: .btn .btn-purple .mr-4 }
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_4_ML1_answers.ipynb){: .btn .btn-purple .mr-4 }


## Images and graph

* Image-based approaches
* Graph-based approaches

[Slides](/files/course/msia_point_clouds/MSIA_Points_5_ML2.pdf){: .btn .btn-purple .mr-4}

#### Practical session
For the practical session, if not working on Google Colab directly, the material can be found on huggingface:
```python
from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="Msun/modelnet40", filename="modelnet40_ply_hdf5_2048.zip", repo_type="dataset", cache_dir=".")
!unzip ./datasets--Msun--modelnet40/snapshots/d5dc795541800feeb7a4b3bd3142729a0d2adf7a/modelnet40_ply_hdf5_2048
```


[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_5_Geometric_Deep_Learning.ipynb){: .btn .btn-purple .mr-4}
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_5_Geometric_Deep_Learning_answers.ipynb){: .btn .btn-purple .mr-4 }

## From convolutions to transformers

* Convolutions on points
* Voxels
* Mixers and transformers

[Slides](/files/course/msia_point_clouds/MSIA_Points_6_ML3.pdf){: .btn .btn-purple .mr-4}

#### Practical session

For the practical session, if not working on Google Colab directly, the material can be found on huggingface:

```python
from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="wangps/shapenet_segmentation", filename="shapenetcore_partanno_segmentation_benchmark_v0_normal.zip", repo_type="dataset", cache_dir=".")
!unzip -qq ./datasets--wangps--shapenet_segmentation/snapshots/dbde146b974e1fc8628b47b1b1c4e50d8bc1a2ef/shapenetcore_partanno_segmentation_benchmark_v0_normal
!mv shapenetcore_partanno_segmentation_benchmark_v0_normal shape_data
```

[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_6_segmentation.ipynb){: .btn .btn-purple .mr-4}

[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_6_segmentation_answers.ipynb){: .btn .btn-purple .mr-4}

## Applications

* Tasks
* Self-supervised training
* Domain adaptation
* Open Vocabulary

[Slides](/files/course/msia_point_clouds/MSIA_Points_7_ML4.pdf){: .btn .btn-purple .mr-4}


```python
import os
if not os.path.exists("./driving.hdf5"):
  !wget https://github.com/aboulch/MSIA_points/releases/download/v0.0.0/driving.tar.gz
  !tar -xvzf driving.tar.gz
```

[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_7_maskclip.ipynb){: .btn .btn-purple .mr-4}
[Notebook (answers)](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_7_maskclip_answers.ipynb){: .btn .btn-purple .mr-4}

## Opening
* Multi-view reconstruction
* NeRFs
* Gaussian splatting
* Dust3R and follow-ups

[Slides](/files/course/msia_point_clouds/MSIA_Points_8_rendering_multiview.pdf){: .btn .btn-purple .mr-4}
[Notebook](https://github.com/aboulch/MSIA_points/blob/main/MSIA_Points_8_ShapeRepresentation.ipynb){: .btn .btn-purple .mr-4}