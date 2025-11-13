---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GoM-Avatar
categories: ["papers"]
tags: ["splats", "smpl", "monocular", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "GoMAvatar: Efficient Animatable Human Modeling from Monocular Video Using Gaussians-on-Mesh"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 17
---

## `GoMAvatar`: Efficient Animatable Human Modeling from Monocular Video Using Gaussians-on-Mesh

> Jing Wen, Xiaoming Zhao, Zhongzheng Ren, Alexander G. Schwing, Shenlong Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="wenj/GoMAvatar" >}}

### Abstract
{{< lead >}}
We introduce GoMAvatar, a novel approach for real-time, memory-efficient, high-quality animatable human modeling. GoMAvatar takes as input a single monocular video to create a digital avatar capable of re-articulation in new poses and real-time rendering from novel viewpoints, while seamlessly integrating with rasterization-based graphics pipelines. Central to our method is the Gaussians-on-Mesh representation, a hybrid 3D model combining rendering quality and speed of Gaussian splatting with geometry modeling and compatibility of deformable meshes. We assess GoMAvatar on ZJU-MoCap data and various YouTube videos. GoMAvatar matches or surpasses current monocular human modeling algorithms in rendering quality and significantly outperforms them in computational efficiency (43 FPS) while being memory-efficient (3.63 MB per subject).
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2404.07991" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="GoM-Avatar teaser"
    caption="`GoM-Avatar` teaser."
    >}}

{{< figure
    src="method.png"
    alt="GoM-Avatar method"
    caption="`GoM-Avatar` method."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="MonoHuman" color="darkmagenta" logo="github" link="https://github.com/Yzmblog/MonoHuman" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Performance

{{<badge label="render" message="23--26ms" color="informational" logo="link" >}}
{{<badge label="render" message="A100" color="informational" logo="link" >}}
