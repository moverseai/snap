---
date: 2023-03-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GNeuVox
categories: ["papers"]
tags: ["smpl", "generalized", "monocular", "arxiv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Generalizable Neural Voxels for Fast Human Radiance Fields"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 8
---

## `GNeuVox`: Generalizable Neural Voxels for Fast Human Radiance Fields

> Taoran Yi, Jiemin Fang, Xinggang Wang, Wenyu Liu

{{< keywordList >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="hustvl/GNeuVox" >}}

### Abstract
{{< lead >}}
Rendering moving human bodies at free viewpoints only from a monocular video is quite a challenging problem. The information is too sparse to model complicated human body structures and motions from both view and pose dimensions. Neural radiance fields (NeRF) have shown great power in novel view synthesis and have been applied to human body rendering. However, most current NeRFbased methods bear huge costs for both training and rendering, which impedes the wide applications in real-life scenarios. In this paper, we propose a rendering framework that can learn moving human body structures extremely quickly from a monocular video. The framework is built by integrating both neural fields and neural voxels. Especially, a set of generalizable neural voxels are constructed. With pretrained on various human bodies, these general voxels represent a basic skeleton and can provide strong geometric priors. For the fine-tuning process, individual voxels are constructed for learning differential textures, complementary to general voxels. Thus learning a novel body can be further accelerated, taking only a few minutes. Our method shows significantly higher training efficiency  compared with previous methods, while maintaining similar rendering quality.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2303.15387" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="GNeuVox overview"
    caption="`GNeuVox` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}

#### Performance
{{<badge label="train" message="15--50mins" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
