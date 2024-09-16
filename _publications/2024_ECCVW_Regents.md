---
layout: publication
title: "ReGentS: Real-World Safety-Critical Driving Scenario Generation Made Stable"
author: "Yuan Yin &ensp
        Pegah Khayatan &ensp
        Éloi Zablocki &ensp
        Alexandre Boulch &ensp
        Matthieu Cord"
permalink: /publications/2024_ECCVW_Regents
date: 2024-09-29
type: conference
venue: "ECCV Workshop on Multimodal Perception and Comprehension of Corner Cases in Autonomous Driving"
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

[Arxiv](https://arxiv.org/abs/2409.07830){: .btn }
[Code](https://github.com/valeoai/ReGentS){: .btn}

### Abstract

Machine learning based autonomous driving systems often face challenges with safety-critical scenarios that are rare in real-world data, hindering their large-scale deployment. While increasing real-world training data coverage could address this issue, it is costly and dangerous. This work explores generating safety-critical driving scenarios by modifying complex real-world regular scenarios through trajectory optimization. We propose ReGentS, which stabilizes generated trajectories and introduces heuristics to avoid obvious collisions and optimization problems. Our approach addresses unrealistic diverging trajectories and unavoidable collision scenarios that are not useful for training robust planner. We also extend the scenario generation framework to handle real-world data with up to 32 agents. Additionally, by using a differentiable simulator, our approach simplifies gradient descent-based optimization involving a simulator, paving the way for future advancements.

