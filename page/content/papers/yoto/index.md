---
date: 2023-03-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: YOTO
categories: ["papers"]
tags: ["smpl", "generalized", "monocular", "arxiv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "You Only Train Once: Multi-Identity Free-Viewpoint Neural Human Rendering from Monocular Videos"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 9
---

## `YOTO`: You Only Train Once: Multi-Identity Free-Viewpoint Neural Human Rendering from Monocular Videos

> Jaehyeok Kim, Dongyoon Wee, Dan Xu

{{< keywordList >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
We introduce You Only Train Once (YOTO), a dynamic human generation framework, which performs freeviewpoint rendering of different human identities with distinct motions, via only one-time training from monocular videos. Most prior works for the task require individualized optimization for each input video that contains a distinct human identity, leading to a significant amount of time and resources for the deployment, thereby impeding the scalability and the overall application potential of the system. In this paper, we tackle this problem by proposing a set of learnable identity codes to expand the capability of the framework for multi-identity free-viewpoint rendering, and an effective pose-conditioned code query mechanism to finely model the pose-dependent non-rigid motions. YOTO optimizes neural radiance fields (NeRF) by utilizing designed identity codes to condition the model for learning various canonical T-pose appearances in a single shared volumetric representation. Besides, our joint learning of multiple identities within a unified model incidentally enables flexible motion transfer in high-quality photo-realistic renderings for all learned appearances. This capability expands its potential use in important applications, including Virtual Reality. We present extensive experimental results on ZJUMoCap and PeopleSnapshot to clearly demonstrate the effectiveness of our proposed model. YOTO shows state-ofthe-art performance on all evaluation metrics while showing significant benefits in training and inference efficiency as well as rendering quality. The code and model will be made publicly available soon.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2303.05835" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="YOTO overview"
    caption="`YOTO` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}

#### Performance
{{<badge label="train" message="A100" color="informational" logo="link" >}}
