---
date: 2022-10-23T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NDF
categories: ["papers"]
tags: ["nerf", "smpl", "eccv22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "NDF: Neural Deformable Fields for Dynamic
Human Modelling"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 6
---

## `NDF`: Neural Deformable Fields for Dynamic Human Modelling

> Ruiqi Zhang, Jie Chen

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="HKBU-VSComputing/2022_ECCV_NDF" >}}

### Abstract
{{< lead >}}
We propose Neural Deformable Fields (NDF), a new representation for dynamic human digitization from a multi-view video. Recent works proposed to represent a dynamic human body with shared canonical neural radiance fields which links to the observation space with deformation fields estimations. However, the learned canonical representation is static and the current design of the deformation fields is not able to represent large movements or detailed geometry changes. In this paper, we propose to learn a neural deformable field wrapped around a fitted parametric body model to represent the dynamic human. The NDF is spatially aligned by the underlying reference surface. A neural network is then learned to map pose to the dynamics of NDF. The proposed NDF representation can synthesize the digitized performer with novel views and novel poses with a detailed and reasonable dynamic appearance. Experiments show that our method significantly outperforms recent human synthesis methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2207.09193" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="NDF overview"
    caption="`NDF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}