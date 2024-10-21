---
date: 2023-10-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: ActorsNeRF
categories: ["papers"]
tags: ["nerf", "smpl", "generalized", "monocular", "iccv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "ActorsNeRF: Animatable Few-shot Human Rendering with Generalizable NeRFs"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 15
---

## `ActorsNeRF`: Animatable Few-shot Human Rendering with Generalizable NeRFs

> Jiteng Mu, Shen Sang, Nuno Vasconcelos, Xiaolong Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="JitengMu/ActorsNeRF" >}}

### Abstract
{{< lead >}}
While NeRF-based human representations have shown impressive novel view synthesis results, most methods still rely on a large number of images / views for training. In this work, we propose a novel animatable NeRF called ActorsNeRF. It is first pre-trained on diverse human subjects, and then adapted with few-shot monocular video frames for a new actor with unseen poses. Building on previous generalizable NeRFs with parameter sharing using a ConvNet encoder, ActorsNeRF further adopts two human priors to capture the large human appearance, shape, and pose variations. Specifically, in the encoded feature space, we will first align different human subjects in a category-level canonical space, and then align the same human from different frames in an instance-level canonical space for rendering. We quantitatively and qualitatively demonstrate that ActorsNeRF significantly outperforms the existing state-of-the-art on few-shot generalization to new people and poses on multiple datasets.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/ICCV2023/papers/Mu_ActorsNeRF_Animatable_Few-shot_Human_Rendering_with_Generalizable_NeRFs_ICCV_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="ActorsNeRF overview"
    caption="`ActorsNeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="AIST++" color="navy" logo="github" link="https://google.github.io/aistplusplus_dataset/factsfigures.html" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="blue" logo="github" link="chungyiweng/HumanNeRF" target="_blank">}}