---
title: "SnapNet: Unstructured point cloud semantic labeling using deep segmentation networks"
collection: publications
permalink: /publications/2017-3DOR-snapnet
excerpt: ''
date: 2017-12-01
venue: 'Computer and Graphics'
paperurl: ''
type: 'journal'
author: 'Alexandre Boulch, Bertrand Le Saux and Nicolas Audebert'
---


Code available at [Github](https://github.com/aboulch/snapnet)

### Computer and Graphics version

[Link to the paper](https://www.sciencedirect.com/science/article/pii/S0097849317301942).

```
@article{boulch2017snapnet,
  title={SnapNet: 3D point cloud semantic labeling with 2D deep segmentation networks},
  author={Boulch, Alexandre and Guerry, Joris and Le Saux, Bertrand and Audebert, Nicolas},
  journal={Computers \& Graphics},
  year={2017},
  publisher={Elsevier}
}
```

### 3DOR Version

A preliminary version of the this work has been presented at 10th Eurographics workshop on 3D Object retrieval, 3DOR 2017.

[Download paper here](https://aboulch.github.io/files/2017_3dor-point.pdf)
```
@inproceedings{boulch2017unstructured,
  title={Unstructured point cloud semantic labeling using deep segmentation networks},
  author={Boulch, Alexandre and Saux, Bertrand Le and Audebert, Nicolas},
  booktitle={Eurographics Workshop on 3D Object Retrieval},
  volume={2},
  year={2017}
}
```

### CODE

The code is available in the dedicated [Github repository](https://github.com/aboulch/snapnet).

The network weights are available to download:

  [RGB model](https://drive.google.com/open?id=0B6IogDVqG75WY0tyWmtzbU1qSDg)

  [Composite model](https://drive.google.com/open?id=0B6IogDVqG75WdVRkNDhjSE5OR0E)

  [Fusion model](https://drive.google.com/open?id=0B6IogDVqG75WRjg2OEVMUmUyRWc) (to be used with RGB and Composite)

  [NPY model of VGG for initialization](https://drive.google.com/open?id=0B6IogDVqG75WUmJYUVV0ZVRjVTA) (based on caffe model VGG 16 from caffe model zoo, converted with Kaffe)