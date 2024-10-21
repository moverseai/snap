---
date: 2023-06-20T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: UVA
categories: ["papers"]
tags: ["nerf", "smpl", "cvpr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "UVA: Towards Unified Volumetric Avatar for View Synthesis, Pose rendering, Geometry and Texture Editing"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 6
---

## `UVA`: Towards Unified Volumetric Avatar for View Synthesis, Pose rendering, Geometry and Texture Editing

> Jinlong Fan, Jing Zhang, Dacheng Tao

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Neural radiance field (NeRF) has become a popular 3D representation method for human avatar reconstruction due to its high-quality rendering capabilities, e.g., regarding novel views and poses. However, previous methods for editing the geometry and appearance of the avatar only allow for global editing through body shape parameters and 2D texture maps. In this paper, we propose a new approach named Unified Volumetric Avatar (UVA) that enables local and independent editing of both geometry and texture, while retaining the ability to render novel views and poses. UVA transforms each observation point to a canonical space using a skinning motion field and represents geometry and texture in separate neural fields. Each field is composed of a set of structured latent codes that are attached to anchor nodes on a deformable mesh in canonical space and diffused into the entire space via interpolation, allowing for local editing. To address spatial ambiguity in code interpolation, we use a local signed height indicator. We also replace the view-dependent radiance color with a pose-dependent shading factor to better represent surface illumination in different poses. Experiments on multiple human avatars demonstrate that our UVA achieves competitive results in novel view synthesis and novel pose rendering while enabling local and independent editing of geometry and appearance.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2304.06969" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.jpg"
    alt="UVA overview"
    caption="`UVA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="A--NeRF" color="orange" logo="github" link="https://github.com/LemonATsu/A-NeRF" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="TAVA" color="coral" logo="github" link="facebookresearch/tava" target="_blank">}}
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}

#### Performance
{{<badge label="train" message="10h" color="informational" logo="link" >}}
{{<badge label="train" message="2_x_V100" color="informational" logo="link" >}}
