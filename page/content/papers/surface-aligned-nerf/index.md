---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: Surface-Aligned-NeRF
categories: ["papers"]
tags: ["nerf", "smpl", "sdf", "cvpr22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Surface-Aligned Neural Radiance Fields for Controllable 3D Human Synthesis"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 16
---

## Surface-Aligned Neural Radiance Fields for Controllable 3D Human Synthesis

> Tianhan Xu, Yasuhiro Fujita, Eiichi Matsumoto

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} SDF {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="pfnet-research/surface-aligned-nerf" >}}

### Abstract
{{< lead >}}
We propose a new method for reconstructing controllable implicit 3D human models from sparse multi-view RGB videos. Our method defines the neural scene representation on the mesh surface points and signed distances from the surface of a human body mesh. We identify an indistinguishability issue that arises when a point in 3D space is mapped to its nearest surface point on a mesh for learning surface-aligned neural scene representation. To address this issue, we propose projecting a point onto a mesh surface using a barycentric interpolation with modified vertex normals. Experiments with the ZJU-MoCap and Human3.6M datasets show that our approach achieves a higher quality in a novel-view and novel-pose synthesis than existing methods. We also demonstrate that our method easily supports the control of body shape and clothes
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2022/papers/Xu_Surface-Aligned_Neural_Radiance_Fields_for_Controllable_3D_Human_Synthesis_CVPR_2022_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="Surface Aligned NeRF overview"
    caption="`Surface Aligned NeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="NARF" color="green" logo="github" link="https://github.com/nogu-atsu/NARF" target="_blank">}}
