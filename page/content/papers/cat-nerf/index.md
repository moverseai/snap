---
date: 2023-06-20T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: CAT-NeRF
categories: ["papers"]
tags: ["nerf", "smpl", "cvpr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "CAT-NeRF: Constancy-Aware Tx2Former for Dynamic Body Modeling"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 11
---

## `CAT-NeRF`: Constancy-Aware Tx2Former for Dynamic Body Modeling

> Haidong Zhu, Zhaoheng Zheng, Wanrong Zheng, Ram Nevatia

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
This paper addresses the problem of human rendering in the video with temporal appearance constancy. Reconstructing dynamic body shapes with volumetric neural rendering methods, such as NeRF, requires finding the correspondence of the points in the canonical and observation space, which demands understanding human body shape and motion. Some methods use rigid transformation, such as SE(3), which cannot precisely model each frame’s unique motion and muscle movements. Others generate the transformation for each frame with a trainable network, such as neural blend weight field or translation vector field, which does not consider the appearance constancy of general body shape. In this paper, we propose CAT-NeRF for self-awareness of appearance constancy with Tx2Former, a novel way to combine two Transformer layers, to separate appearance constancy and uniqueness. Appearance constancy models the general shape across the video, and uniqueness models the unique patterns for each frame. We further introduce a novel Covariance Loss to limit the correlation between each pair of appearance uniquenesses to ensure the frame-unique pattern is maximally captured in appearance uniqueness. We assess our method on H36M and ZJU-MoCap and show state-of-the-art performance.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2023W/DynaVis/papers/Zhu_CAT-NeRF_Constancy-Aware_Tx2Former_for_Dynamic_Body_Modeling_CVPRW_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="CAT-NeRF overview"
    caption="`CAT-NeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="blue" logo="github" link="chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}

#### Performance
{{<badge label="train" message="20--30h" color="informational" logo="link" >}}
{{<badge label="train" message="A100" color="informational" logo="link" >}}
