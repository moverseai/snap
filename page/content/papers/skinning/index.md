---
date: 2025-09-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SkinnedGaussianAvatars
categories: ["papers"]
tags: ["splats", "smpl", "smplx", "monocular", "euroxr25"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "On the Skinning of Gaussian Avatars"
summary: TODO
keywords: #
type: '2025' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2025"]
series_order: 3
---

## On the Skinning of Gaussian Avatars

> Nikolaos Zioulis, Nikolaos Kotarelas, Georgios Albanis, Spyridon Thermos, Anargyros Chatzitofis

{{< keywordList >}}
{{< keyword icon="tag" >}} Splats {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL-X {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *EuroXR* 2025 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="moverseai/snap" >}}

### Abstract
{{< lead >}}
Radiance field-based methods have recently been used to reconstruct human avatars, showing that we can significantly downscale the systems needed for creating animated human avatars. Although this progress has been initiated by neural radiance fields, their slow rendering and backward mapping from the observation space to the canonical space have been the main challenges. With Gaussian splatting overcoming both challenges, a new family of approaches has emerged that are faster to train and render, while also straightforward to implement using forward skinning from the canonical to the observation space. However, the linear blend skinning required for the deformation of the Gaussians does not provide valid results for their nonlinear rotation properties. To address such artifacts, recent works use mesh properties to rotate the non-linear Gaussian properties or train models to predict corrective offsets. Instead, we propose a weighted rotation blending approach that leverages quaternion averaging. This leads to simpler vertex-based Gaussians that can be efficiently animated and integrated in any engine by only modifying the linear blend skinning technique, and using any Gaussian rasterizer.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2509.11411" target="_blank" >}}
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
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}
{{<badge label="test" message="NeuMan" color="white" logo="github" link="https://github.com/apple/ml-neuman" target="_blank">}}
{{<badge label="test" message="GalaBasketball" color="blanchedalmond" logo="github" link="https://github.com/jimmyYliu/Animatable-3D-Gaussian" target="_blank">}}

#### Comparisons
{{<badge label="body--Splats" message="HUGS" color="brown" logo="github" link="https://github.com/apple/ml-hugs" target="_blank">}}
{{<badge label="body--Splats" message="iHuman" color="crimson" logo="github" link="https://github.com/pramishp/ihuman" target="_blank">}}
{{<badge label="body--Splats" message="SplattingAvatar" color="lemonchiffon" logo="github" link="https://github.com/initialneil/SplattingAvatar" target="_blank">}}
{{<badge label="body--Splats" message="Animatable3DGaussians" color="blanchedalmond" logo="github" link="https://github.com/jimmyYliu/Animatable-3d-Gaussian" target="_blank">}}
{{<badge label="body--Splats" message="HAHA" color="azure" logo="github" link="https://github.com/david-svitov/HAHA" target="_blank">}}

#### Performance
{{<badge label="train" message="30m" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3080Ti" color="informational" logo="link" >}}

{{<badge label="render" message="2ms" color="informational" logo="link" >}}