---
date: 2024-12-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SAGA
categories: ["papers"]
tags: ["splats", "smpl", "arxiv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "SAGA: Surface-Aligned Gaussian Avatar"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 19
---

## `SAGA`: Surface-Aligned Gaussian Avatar

> Mingwei Li, Jiachen Tao, Zongxin Yang, Yi Yang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *arXiv* 2024 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
This paper presents a Surface-Aligned Gaussian representation for creating animatable human avatar from monocular video, aiming at improving the novel view and pose synthesis performance while ensuring fast training and real-time rendering. Recently, 3D Gaussian Splatting (3DGS) has emerged as a more efficient and expressive alternative to neural radiance fields, and has been used for creating dynamic human avatar. However, when applied to the severely ill-posed task of monocular reconstruction, the transient regions such as clothes wrinkles or shadows that change constantly cannot provide consistent supervision for the Gaussians, resulting in noisy geometry and abrupt deformation that typically fail to generalize under novel views and poses. To address these limitations, we present SAGA, i.e., Surface-Aligned Gaussian Avatar, which aligns the Gaussians with a mesh to enforce well-defined geometry and consistent deformation, thereby improving generalization under novel views and poses. Unlike existing strict alignment methods that suffer from limited expressive power and low realism, SAGA employs a two-stage alignment strategy where the Gaussians are first adhered on while then detached from the mesh, thus facilitating both good geometry and high expressivity. In the first stage, we improve the flexibility of Adhered-on-Mesh Gaussians by allowing them to flow on the mesh, in contrast to existing methods that rigidly bind Gaussians to fixed location. In the second stage, we introduce a Gaussian-Mesh Alignment regularization that constrains the geometry and deformation of the detached Gaussians by minimizing their location and orientation offset from the bound triangle. Finally, an efficient Walking-on-Mesh strategy is introduced to dynamically update the bound triangle as Gaussians drift outside, ensuring accurate regularization even as the geometry evolves. Experiments on challenging datasets demonstrate that SAGA outperforms both NeRF and Gaussian-based methods on novel view and pose synthesis tasks, with state-of-the-art training time of 12 minutes, and real-time rendering efficiency at 60+ FPS. Additionally, we showcase that SAGA enables direct high-quality mesh extraction from Gaussians, marking the first attempt at deformable Gaussians learned from monocular human video.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2412.00845" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.png"
    alt="SAGA overview"
    caption="`SAGA` overview."
    >}}

{{< figure
    src="method2.png"
    alt="SAGA details"
    caption="`SAGA` details."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DeepCap" color="cyan" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="InstantNVR" color="fuchsia" logo="github" link="https://github.com/zju3dv/instant-nvr" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--Splats" message="GauHuman" color="chocolate" logo="github" link="https://github.com/skhu101/GauHuman" target="_blank">}}
{{<badge label="body--Splats" message="GoMAvatar" color="bisque" logo="github" link="https://github.com/wenj/GoMAvatar" target="_blank">}}

#### Performance
{{<badge label="train" message="12m" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}

{{<badge label="render" message="16ms" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3090" color="informational" logo="link" >}}