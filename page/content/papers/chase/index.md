---
date: 2024-08-07T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: CHASE
categories: ["papers"]
tags: ["splats", "smpl", "deformation", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "CHASE: 3D-Consistent Human Avatars with Sparse Inputs via Gaussian Splatting and Contrastive Learning"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 25
---

## `CHASE`: 3D-Consistent Human Avatars with Sparse Inputs via Gaussian Splatting and Contrastive Learning

> Haoyu Zhao, Hao Wang, Chen Yang, Wei Shen

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

<!-- {{< github repo="user/repo" >}} -->

### Abstract
{{< lead >}}
Existing approaches for human avatar generation–both NeRF-based and 3D Gaussian Splatting (3DGS) based–struggle with maintaining 3D consistency and exhibit degraded detail reconstruction, particularly when training with sparse inputs. To address this challenge, we propose CHASE, a novel framework that achieves dense-input-level performance using only sparse inputs through two key innovations: cross-pose intrinsic 3D consistency supervision and 3D geometry contrastive learning. Building upon prior skeleton-driven approaches that combine rigid deformation with non-rigid cloth dynamics, we first establish baseline avatars with fundamental 3D consistency. To enhance 3D consistency under sparse inputs, we introduce a Dynamic Avatar Adjustment (DAA) module, which refines deformed Gaussians by leveraging similar poses from the training set. By minimizing the rendering discrepancy between adjusted Gaussians and reference poses, DAA provides additional supervision for avatar reconstruction. We further maintain global 3D consistency through a novel geometry-aware contrastive learning strategy. While designed for sparse inputs, CHASE surpasses state-of-the-art methods across both full and sparse settings on ZJU-MoCap and H36M datasets, demonstrating that our enhanced 3D consistency leads to superior rendering quality. 
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2408.09663" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="CHASE teaser"
    caption="`CHASE` teaser."
    >}}

{{< figure
    src="overview.jpg"
    alt="CHASE overview"
    caption="`CHASE` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="NARF" color="green" logo="github" link="https://github.com/nogu-atsu/NARF" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="MonoHuman" color="darkmagenta" logo="github" link="https://github.com/Yzmblog/MonoHuman" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}
{{<badge label="body--Splats" message="GoMAvatar" color="bisque" logo="github" link="https://github.com/wenj/GoMAvatar" target="_blank">}}
