---
date: 2022-06-21T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HumanNeRF-2
categories: ["papers"]
tags: ["nerf", "smpl", "cvpr22", "generalized"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "HumanNeRF: Efficiently Generated Human Radiance Field from Sparse Inputs"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 2
---

## `HumanNeRF`: Efficiently Generated Human Radiance Field from Sparse Inputs

> Fuqiang Zhao, Wei Yang, Jiakai Zhang, Pei Lin, Yingliang Zhang, Jingyi Yu, Lan Xu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="zhaofuq/HumanNeRF" >}}

### Abstract
{{< lead >}}
Recent neural human representations can produce highquality multi-view rendering but require using dense multiview inputs and costly training. They are hence largely limited to static models as training each frame is infeasible. We present HumanNeRF - a neural representation with efficient generalization ability - for high-fidelity free-view synthesis of dynamic humans. Analogous to how IBRNet assists NeRF by avoiding per-scene training, HumanNeRF employs an aggregated pixel-alignment feature across multiview inputs along with a pose embedded non-rigid deformation field for tackling dynamic motions. The raw HumanNeRF can already produce reasonable rendering on sparse video inputs of unseen subjects and camera settings. To further improve the rendering quality, we augment our solution with in-hour scene-specific fine-tuning, and an appearance blending module for combining the benefits of both neural volumetric rendering and neural texture blending. Extensive experiments on various multi-view dynamic human datasets demonstrate effectiveness of our approach in synthesizing photo-realistic free-view humans under challenging motions and with very sparse camera view inputs.

{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2112.02789.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="HumanNeRF overview"
    caption="`HumaNeRF` overview."
    >}}
{{< figure
    src="method2.png"
    alt="HumanNeRF rendering"
    caption="`HumaNeRF` rendering."
    >}}

### Results

#### Data
{{<badge label="test" message="Twindom" color="yellowgreen" logo="google" logoColor="white" link="https://drive.google.com/drive/folders/1P3OyAjTNh1V74OSPf0JJ1OnF-E6oklKB" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="30--90h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}