---
date: 2022-10-23T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Relighting4D
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "eccv22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "Relighting4D: Neural Relightable Human from Videos"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 19
---

## `Relighting4D`: Neural Relightable Human from Videos

> Zhaoxi Chen, Ziwei Liu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL  {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="FrozenBurning/Relighting4D" >}}

### Abstract
{{< lead >}}
Human relighting is a highly desirable yet challenging task. Existing works either require expensive one-light-at-a-time (OLAT) captured data using light stage or cannot freely change the viewpoints of the rendered body. In this work, we propose a principled framework, Relighting4D, that enables free-viewpoints relighting from only human videos under unknown illuminations. Our key insight is that the spacetime varying geometry and reflectance of the human body can be decomposed as a set of neural fields of normal, occlusion, diffuse, and specular maps. These neural fields are further integrated into reflectance-aware physically based rendering, where each vertex in the neural field absorbs and reflects the light from the environment. The whole framework can be learned from videos in a self-supervised manner, with physically informed priors designed for regularization. Extensive experiments on both real and synthetic datasets demonstrate that our framework is capable of relighting dynamic human actors with free-viewpoints.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2207.07104" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="Relighting4D overview"
    caption="`Relighting4D` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="V100" color="informational" logo="link" >}}