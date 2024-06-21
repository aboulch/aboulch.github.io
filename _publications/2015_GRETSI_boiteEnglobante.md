---
layout: publication
title: "Un générateur de boites englobantes parcimonieux pour la détection d'objets dans des vidéos"
author: 'A. Chan-Hon-Tong, S. Herbin and A. Boulch'
permalink: /publications/2015_gretsi_generator
date: 2015-01-01
type: conference
venue: 'XXV colloque Gretsi'
paperurl: 
arxivurl: 
halurl: 'https://hal.archives-ouvertes.fr/hal-01175556/document'
codeurl: 
mediumurl: 
blogurl: 
pdfurl: 
slidesurl: 
teaser: /files/2015-GRETSI-boxes.png
note:
noteimportant:
---

### Abstract

The ability to automatically detect object in video stream while dealing with computation time constraint is still not reached by
the state of the art algorithms. However, some applications need only the detection of each object at least one time, but not necessarily, the
detection of each object in each frame. This context allows to soften algorithmic constraints. Particularly, in this paper, we offer a bounding
box proposal algorithm designed to recover each target at least one time in the video with a very small set of boxes per frame. This algorithm
achieves interesting result on the VIRAT aerial dataset while handling more than 25 frames per second.

### Résumé

La capacité à détecter automatiquement des objets dans des flux vidéos en respectant des contraintes de temps de calcul semble encore
aujourd’hui hors d’atteinte. Cependant, beaucoup d’applications nécessitent seulement de détecter chaque objet dans au moins une image, et non
pas, de détecter chaque objet dans chaque image. En tenant compte de cette spécificité, nous proposons un algorithme de proposition de boites
englobantes dont l’objectif est de recouvrir au moins une fois chaque objet en ne proposant qu’un très faible nombre de boites par image. Notre
algorithme obtient des résultats intéressants sur le jeu de données VIRAT aerial tout en respectant largement les contraintes de temps réel.