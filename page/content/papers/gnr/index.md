---
date: 2022-04-20T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GNR
categories: ["papers"]
tags: ["nerf", "smplx", "sdf", "generalized", "arxiv22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Generalizable Neural Performer: Learning Robust Radiance Fields for Human Novel View Synthesis"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 12
---

## `Generalizable Neural Performer`: Learning Robust Radiance Fields for Human Novel View Synthesis

> Wei Cheng, Su Xu, Jingtan Piao, Chen Qian, Wayne Wu,Kwan-Yee Lin, Hongsheng Li

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} SDF {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="generalizable-neural-performer/gnr" >}}

### Abstract
{{< lead >}}
This work targets at using a general deep learning framework to synthesize free-viewpoint images of arbitrary human performers, only requiring a sparse number of camera views as inputs and skirting per-case fine-tuning. The large variation of geometry and appearance, caused by articulated body poses, shapes and clothing types, are the key bot tlenecks of this task. To overcome these challenges, we present a simple yet powerful framework, named Generalizable Neural Performer (GNR), that learns a generalizable and robust neural body representation over various geometry and appearance. Specifically, we compress the light fields for novel view human rendering as conditional implicit neural radiance fields with several designs from both geometry and appearance aspects. We first introduce an Implicit Geometric Body Embedding strategy to enhance the robustness based on both parametric 3D human body model prior and multi-view source images hints. On the top of this, we further propose a Screen-Space Occlusion-Aware Appearance Blending technique to preserve the high-quality appearance, through interpolating source view appearance to the radiance fields with a relax but approximate geometric guidance.

To evaluate our method, we present our ongoing effort of constructing a dataset with remarkable complexity and diversity. The first dataset version, GeneBody-1.0, includes over 2.95M frames of 100 subjects performing 370 sequences under multi-view cameras capturing, performing a large variety of pose actions, along with diverse body shapes, clothing, accessories and hairdos. Experiments on GeneBody-1.0 and ZJU-Mocap show better robustness of our methods than recent state-of-the-art generalizable methods among all cross-dataset, unseen subjects and unseen poses settings. We also demonstrate the competitiveness of our model compared with cutting-edge case-specific ones. Dataset, code and model will be made publicly available.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2204.11798" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="GNR overview"
    caption="`GNR` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}
{{<badge label="test" message="GeneBody" color="violet" logo="link" link="https://generalizable-neural-performer.github.io/genebody.html" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="A--NeRF" color="orange" logo="github" link="https://github.com/LemonATsu/A-NeRF" target="_blank">}}

#### Performance
{{<badge label="train" message="8_x_V100" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="160ms" color="informational" logo="link" >}}