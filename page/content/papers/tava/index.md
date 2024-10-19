---
date: 2022-10-23T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: TAVA
categories: ["papers"]
tags: ["nerf", "skeleton", "eccv22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "TAVA: Template-free Animatable Volumetric Actors"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 7
---

## `TAVA`: Template-free Animatable Volumetric Actors

> Ruilong Li, Julian Tanke, Minh Vo, Michael Zollhoefer, Jürgen Gall, Angjoo Kanazawa, Christoph Lassner

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="facebookresearch/tava" >}}

### Abstract
{{< lead >}}
Coordinate-based volumetric representations have the potential to generate photo-realistic virtual avatars from images. However, virtual avatars also need to be controllable even to a novel pose that may not have been observed. Traditional techniques, such as LBS, provide such a function; yet it usually requires a hand-designed body template, 3D scan data, and limited appearance models. On the other hand, neural representation has been shown to be powerful in representing visual details, but are under explored on deforming dynamic articulated actors. In this paper, we propose TAVA, a method to create Template-free Animatable Volumetric Actors, based on neural representations. We rely solely on multi-view data and a tracked skeleton to create a volumetric model of an actor, which can be animated at the test time given novel pose. Since TAVA does not require a body template, it is applicable to humans as well as other creatures such as animals. Furthermore, TAVA is designed such that it can recover accurate dense correspondences, making it amenable to content-creation and editing tasks. Through extensive experiments, we demonstrate that the proposed method generalizes well to novel poses as well as unseen views and showcase basic editing capabilities. 
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2206.08929" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.jpg"
    alt="TAVA overview"
    caption="`TAVA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="A--NeRF" color="orange" logo="github" link="https://github.com/LemonATsu/A-NeRF" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="NARF" color="green" logo="github" link="https://github.com/nogu-atsu/NARF" target="_blank">}}
