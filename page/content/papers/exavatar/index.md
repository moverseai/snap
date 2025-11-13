---
date: 2024-10-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: ExAvatar
categories: ["papers"]
tags: ["splats", "smplx", "monocular", "eccv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Expressive Whole-Body 3D Gaussian Avatar"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 12
---

## `ExAvatar`: Expressive Whole-Body 3D Gaussian Avatar

> Gyeongsik Moon, Takaaki Shiratori, Shunsuke Saito

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ECCV* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="mks0601/ExAvatar_RELEASE" >}}

### Abstract
{{< lead >}}
Facial expression and hand motions are necessary to express our emotions and interact with the world. Nevertheless, most of the 3D human avatars modeled from a casually captured video only support body motions without facial expressions and hand motions. In this work, we present ExAvatar, an expressive whole-body 3D human avatar learned from a short monocular video. We design ExAvatar as a combination of the whole-body parametric mesh model (SMPL-X) and 3D Gaussian Splatting (3DGS). The main challenges are 1) a limited diversity of facial expressions and poses in the video and 2) the absence of 3D observations, such as 3D scans and RGBD images. The limited diversity in the video makes animations with novel facial expressions and poses non-trivial. In addition, the absence of 3D observations could cause significant ambiguity in human parts that are not observed in the video, which can result in noticeable artifacts under novel motions. To address them, we introduce our hybrid representation of the mesh and 3D Gaussians. Our hybrid representation treats each 3D Gaussian as a vertex on the surface with pre-defined connectivity information (i.e., triangle faces) between them following the mesh topology of SMPL-X. It makes our ExAvatar animatable with novel facial expressions by driven by the facial expression space of SMPL-X. In addition, by using connectivity-based regularizers, we significantly reduce artifacts in novel facial expressions and poses.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2407.21686" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="method.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="X--Humans" color="goldenrod" logo="github" link="https://xhumans.ait.ethz.ch/" target="_blank">}}
{{<badge label="test" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="HUGS" color="brown" logo="github" link="https://github.com/apple/ml-hugs" target="_blank">}}
{{<badge label="body--Splats" message="GaussianAvatar" color="green" logo="github" link="https://github.com/aipixel/GaussianAvatar" target="_blank">}}
{{<badge label="body--NeRF" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}
{{<badge label="body--NeRF" message="Vid2Avatar" color="palegreen" logo="github" link="https://github.com/MoyGcc/vid2avatar" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="purple" logo="github" link="https://github.com/chungyiweng/HumanNeRF" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
{{<badge label="body--Splats" message="3DGS--Avatar" color="teal" logo="github" link="https://github.com/mikeqzy/3dgs-avatar-release" target="_blank">}}
{{<badge label="body--NeRF" message="X--Avatar" color="rebeccapurple" logo="github" link="https://github.com/Skype-line/X-Avatar" target="_blank">}}

#### Performance
{{<badge label="train" message="V100" color="informational" logo="link" >}}
{{<badge label="train" message="1.5--5h" color="informational" logo="link" >}}

{{<badge label="render" message="V100" color="informational" logo="link" >}}
{{<badge label="render" message="1024_x_1024" color="informational" logo="link" >}}
{{<badge label="render" message="38ms" color="informational" logo="link" >}}