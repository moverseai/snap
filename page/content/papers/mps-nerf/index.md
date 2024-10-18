---
date: 2022-09-23T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: MPS-NeRF
categories: ["papers"]
tags: ["nerf", "smpl", "generalized", "tpami22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "MPS-NeRF: Generalizable 3D Human Rendering from Multiview Images"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 18
---

## `MPS-NeRF`: Generalizable 3D Human Rendering from Multiview Images

> Xiangjun Gao, Jiaolong Yang, Jongyoo Kim, Sida Peng, Zicheng Liu, Xin Tong

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *TPAMI* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="gaoxiangjun/MPS-NeRF" >}}

### Abstract
{{< lead >}}
There has been rapid progress recently on 3D human rendering, including novel view synthesis and pose animation, based on the advances of neural radiance fields (NeRF). However, most existing methods focus on person-specific training and their training typically requires multi-view videos. This paper deals with a new challenging task – rendering novel views and novel poses for a person unseen in training, using only multiview still images as input without videos. For this task, we propose a simple yet surprisingly effective method to train a generalizable NeRF with multiview images as conditional input. The key ingredient is a dedicated representation combining a canonical NeRF and a volume deformation scheme. Using a canonical space enables our method to learn shared properties of human and easily generalize to different people. Volume deformation is used to connect the canonical space with input and target images and query image features for radiance and density prediction. We leverage the parametric 3D human model fitted on the input images to derive the deformation, which works quite well in practice when combined with our canonical NeRF. The experiments on both real and synthetic data with the novel view synthesis and pose animation tasks collectively demonstrate the efficacy of our method.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2203.16875" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="MPS-NeRF overview"
    caption="`MPS-NeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}
{{<badge label="test" message="THuman" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/DeepHuman/tree/master/THUmanDataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}

#### Performance
{{<badge label="train" message="2d" color="informational" logo="link" >}}
{{<badge label="train" message="2_x_V100" color="informational" logo="link" >}}
