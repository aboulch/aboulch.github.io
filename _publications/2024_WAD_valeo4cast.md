---
layout: publication
title: "Valeo4Cast: A Modular Approach to End-to-End Forecasting"
author: "Yihong Xu &ensp; 
         Éloi Zablocki &ensp;
         Alexandre Boulch &ensp;
         Gilles Puy &ensp;
         Mickaël Chen &ensp;
         Florent Bartoccioni &ensp;
         Nermin Samet &ensp;
         Oriane Siméoni &ensp;
         Spyros Gidaris &ensp;
         Tuan-Hung Vu &ensp;
         Andrei Bursuc &ensp;
         Eduardo Valle &ensp;
         Renaud Marlet &ensp;
         Matthieu Cord"
permalink: /publications/2024_WAD_valeo4cast
date: 2024-06-17
type: conference
venue: "CVPR Workshop on Autonomous Driving (WAD)"
paperurl: 
arxivurl:
halurl: 
codeurl: 
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser:
note:
noteimportant: 
---

[Arxiv](https://arxiv.org/abs/2406.08113){: .btn }

![Valeo4Cast teaser](/images/publications/2024_CVPR_WAD_valeo4cast/teaser.png)

### Abstract

Motion forecasting is crucial in autonomous driving systems to anticipate the future trajectories of surrounding agents such as pedestrians, vehicles, and traffic signals. In end-to-end forecasting, the model must jointly detect from sensor data (cameras or LiDARs) the position and past trajectories of the different elements of the scene and predict their future location. We depart from the current trend of tackling this task via end-to-end training from perception to forecasting and we use a modular approach instead. Following a recent study, we individually build and train detection, tracking, and forecasting modules. We then only use consecutive finetuning steps to integrate the modules better and alleviate compounding errors. Our study reveals that this simple yet effective approach significantly improves performance on the end-to-end forecasting benchmark. Consequently, our solution ranks first in the Argoverse 2 end-to-end Forecasting Challenge held at CVPR 2024 Workshop on Autonomous Driving (WAD), with 63.82 mAPf. We surpass forecasting results by +17.1 points over last year's winner and by +13.3 points over this year's runner-up. This remarkable performance in forecasting can be explained by our modular paradigm, which integrates finetuning strategies and significantly outperforms the end-to-end-trained counterparts.

### Citation


```
@article{xu2024valeo4cast,
  title      = {Valeo4Cast: A Modular Approach to End-to-End Forecasting},
  author     = {Yihong Xu and
                Eloi Zablocki and
                Alexandre Boulch and
                Gilles Puy and
                Mickael Chen and
                Florent Bartoccioni and
                Nermin Samet and
                Oriane Simeoni and
                Spyros Gidaris and
                Tuan-Hung Vu and
                Andrei Bursuc and
                Eduardo Valle and
                Renaud Marlet and
                Matthieu Cord},
  journal = {Winning solution to the "Unified Detection, Tracking and Forecasting" Argoverse 2 challenge @CVPR Worshop on Autonomous Driving (WAD)},
  year    = {2024}
}
```