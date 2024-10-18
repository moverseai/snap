---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: H-NeRF
categories: ["papers"]
tags: ["nerf", "ghum", "sdf", "neurips21"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: Neural Radiance Fields for Rendering and Temporal Reconstruction of Humans in Motion
summary: Constrained by a structured implicit human body model, represented using signed distance functions, `H-NeRF` robustly fuses information from sparse views and generalizes well beyond the poses or views observed in training. 
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 4
---

## `H-NeRF`: Neural Radiance Fields for Rendering and Temporal Reconstruction of Humans in Motion

> Hongyi Xu, Thiemo Alldieck, Cristian Sminchisescu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} GHUM {{< /keyword >}}
{{< keyword icon="tag" >}} SDF {{< /keyword >}}
{{< keyword icon="email" >}} *NeurIPS* 2021 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
We present neural radiance fields for rendering and temporal (4D) reconstruction of humans in motion (H-NeRF), as captured by a sparse set of cameras or even from a monocular video. Our approach combines ideas from neural scene representation, novel-view synthesis, and implicit statistical geometric human representations, coupled using novel loss functions. Instead of learning a radiance field with a uniform occupancy prior, we constrain it by a structured implicit human body model, represented using signed distance functions. This allows us to robustly fuse information from sparse views and generalize well beyond the poses or views observed in training. Moreover, we apply geometric constraints to co-learn the structure of the observed subject – including both body and clothing – and to regularize the radiance field to geometrically plausible solutions. Extensive experiments on multiple datasets demonstrate the robustness and the accuracy of our approach, its generalization capabilities significantly outside a small training set of poses and views, and statistical extrapolation beyond the observed shape.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2110.13746" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="H-NeRF overview"
    caption="`H-NeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}
{{<badge label="test" message="GHS3D" color="yellow" logo="github" link="https://github.com/google-research/google-research/tree/master/ghum" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="6--8h" color="informational" logo="link" >}}
{{<badge label="train" message="8_x_V100" color="informational" logo="link" >}}
{{<badge label="render" message="9sec" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="V100" color="informational" logo="link" >}}