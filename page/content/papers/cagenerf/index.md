---
date: 2022-11-28T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: CageNeRF
categories: ["papers"]
tags: ["nerf", "deformation", "neurips22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "CageNeRF: Cage-based Neural Radiance Fields for Genrenlized 3D Deformation and Animation"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 5
---

## `CageNeRF`: Cage-based Neural Radiance Fields for Genrenlized 3D Deformation and Animation

> Yicong Peng, Yichao Yan, Shenqi Liu, Yuhao Cheng, Shanyan Guan, Bowen Pan, Guangtao Zhai, Xiaokang Yang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *NeurIPS* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="PengYicong/CageNeRF" >}}

### Abstract
{{< lead >}}
While implicit representations have achieved high-fidelity results in 3D rendering, deforming and animating the implicit field remains challenging. Existing works typically leverage data-dependent models as deformation priors, such as SMPL for human body animation. However, this dependency on category-specific priors limits them to generalize to other objects. To solve this problem, we propose a novel framework for deforming and animating the neural radiance field learned on arbitrary objects. The key insight is that we introduce a cage-based representation as deformation prior, which is category-agnostic. Specifically, the deformation is performed based on an enclosing polygon mesh with sparsely defined vertices called cage inside the rendering space, where each point is projected into a novel position based on the barycentric interpolation of the deformed cage vertices. In this way, we transform the cage into a generalized constraint, which is able to deform and animate arbitrary target objects while preserving geometry details. Based on extensive experiments, we demonstrate the effectiveness of our framework in the task of geometry editing, object animation and deformation transfer.
{{< /lead >}}

{{< button href="https://proceedings.neurips.cc/paper_files/paper/2022/file/cb78e6b5246b03e0b82b4acc8b11cc21-Paper-Conference.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.png"
    alt="CageNeRF overview"
    caption="`CageNeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}