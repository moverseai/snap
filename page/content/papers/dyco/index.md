---
date: 2024-10-07T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: DyCo
categories: ["papers"]
tags: ["nerf", "skeleton", "deformation", "eccv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "Within the Dynamic Context: Inertia-aware 3D Human Modeling with Pose Sequence"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 36
---

## Within the Dynamic Context: Inertia-aware 3D Human Modeling with Pose Sequence

> Yutong Chen, Yifan Zhan, Zhihang Zhong, Wei Wang, Xiao Sun, Yu Qiao, Yinqiang Zheng

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="Yifever20002/Dyco" >}}

### Abstract
{{< lead >}}
Neural rendering techniques have significantly advanced 3D human body modeling. However, previous approaches often overlook dynamics induced by factors such as motion inertia, leading to challenges in scenarios like abrupt stops after rotation, where the pose remains static while the appearance changes. This limitation arises from reliance on a single pose as conditional input, resulting in ambiguity in mapping one pose to multiple appearances. In this study, we elucidate that variations in human appearance depend not only on the current frame's pose condition but also on past pose states. Therefore, we introduce Dyco, a novel method utilizing the delta pose sequence representation for non-rigid deformations and canonical space to effectively model temporal appearance variations. To prevent a decrease in the model's generalization ability to novel poses, we further propose low-dimensional global context to reduce unnecessary inter-body part dependencies and a quantization operation to mitigate overfitting of the delta pose sequence by the model. To validate the effectiveness of our approach, we collected a novel dataset named I3D-Human, with a focus on capturing temporal changes in clothing appearance under approximate poses. Through extensive experiments on both I3D-Human and existing datasets, our approach demonstrates superior qualitative and quantitative performance. In addition, our inertia-aware 3D human method can unprecedentedly simulate appearance changes caused by inertia at different velocities.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2403.19160" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="DyCo teaser"
    caption="`DyCo` teaser."
    >}}

{{< figure
    src="method.png"
    alt="DyCo overview"
    caption="`DyCo` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="I3D--Human" color="lemonchiffon" logo="link" link="https://github.com/Yifever20002/Dyco" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}

#### Performance
{{<badge label="train" message="12h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX2080" color="informational" logo="link" >}}
