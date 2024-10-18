---
date: 2021-06-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Anim-NeRF
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "arxiv21"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: Animatable Neural Radiance Fields from Monocular RGB Videos
summary: TODO 
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 2
---

## `Anim-NeRF`: Animatable Neural Radiance Fields from Monocular RGB Videos

> Jianchuan Chen, Ying Zhang, Di Kang, Xuefei Zhe, Linchao Bao, Xu Jia, Huchuan Lu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2021 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="JanaldoChen/Anim-NeRF" >}}

### Abstract
{{< lead >}}
We present animatable neural radiance fields (animatable `NeRF`) for detailed human avatar creation from monocular videos. Our approach extends neural radiance fields (`NeRF`) to the dynamic scenes with human movements via introducing explicit pose-guided deformation while learning the scene representation network. In particular, we estimate the human pose for each frame and learn a constant canonical space for the detailed human template, which enables natural shape deformation from the observation space to the canonical space under the explicit control of the pose parameters. To compensate for inaccurate pose estimation, we introduce the pose refinement strategy that updates the initial pose during the learning process, which not only helps to learn more accurate human reconstruction but also accelerates the convergence. In experiments we show that the proposed approach achieves **1)** implicit human geometry and appearance reconstruction with high-quality details, **2)** photo-realistic rendering of the human from novel views, and **3)** animation of the human with novel poses.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2106.13629" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.png"
    alt="Anim-NeRF overview"
    caption="`Anim-NeRF` overview."
    >}}

### Results

#### Data

{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}
{{<badge label="test" message="iPER" color="critical" logo="github" link="https://svip-lab.github.io/dataset/iPER_dataset.html" target="_blank">}}
{{<badge label="test" message="MultiGarment" color="coral" logo="link" link="https://virtualhumans.mpi-inf.mpg.de/mgn/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="13h" color="informational" logo="link" >}}
{{<badge label="train" message="2_x_RTX3090" color="informational" logo="link" >}}