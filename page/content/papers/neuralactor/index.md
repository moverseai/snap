---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NeuralActor
categories: ["papers"]
tags: ["nerf", "smpl", "texture", "siggraph_asia21"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Neural Actor: Neural Free-view Synthesis of Human Actors with Pose Control"
summary: TODO
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 7
---

## `Neural Actor`: Neural Free-view Synthesis of Human Actors with Pose Control

> Lingjie Liu, Marc Habermann, Viktor Rudnev, Kripasindhu Sarkar, Jiatao Gu, Christian Theobalt

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH Asia* 2021 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="lingjie0206/Neural_Actor_Main_Code" >}}

### Abstract
{{< lead >}}
We propose Neural Actor (NA), a new method for high-quality synthesis of humans from arbitrary viewpoints and under arbitrary controllable poses. Our method is built upon recent neural scene representation and rendering works which learn representations of geometry and appearance from only 2D images. While existing works demonstrated compelling rendering of static scenes and playback of dynamic scenes, photo-realistic reconstruction and rendering of humans with neural implicit methods, in particular under user-controlled novel poses, is still difficult. To address this problem, we utilize a coarse body model as the proxy to unwarp the surrounding 3D space into a canonical pose. A neural radiance field learns pose-dependent geometric deformations and pose- and view-dependent appearance effects in the canonical space from multi-view video input. To synthesize novel views of high fidelity dynamic geometry and appearance, we leverage 2D texture maps defined on the body model as latent variables for predicting residual deformations and the dynamic appearance. Experiments demonstrate that our method achieves better quality than the state-of-the-arts on playback as well as novel pose synthesis, and can even generalize well to new poses that starkly differ from the training poses. Furthermore, our method also supports body shape control of the synthesized results.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2106.02019" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="Neural Actor overview"
    caption="`Neural Actor` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="DeepCap" color="cyan" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="NeuralActor" color="brightgreen" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="AIST++" color="navy" logo="github" link="https://google.github.io/aistplusplus_dataset/factsfigures.html" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="4d" color="informational" logo="link" >}}
{{<badge label="train" message="8_x_V100" color="informational" logo="link" >}}
{{<badge label="render" message="4sec" color="informational" logo="link" >}}
{{<badge label="render" message="940_x_1285" color="informational" logo="link" >}}
