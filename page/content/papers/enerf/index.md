---
date: 2022-12-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: ENeRF
categories: ["papers"]
tags: ["nerf", "siggraph_asia22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Efficient Neural Radiance Fields for Interactive Free-viewpoint Video"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 26
---

## `ENeRF`: Efficient Neural Radiance Fields for Interactive Free-viewpoint Video

> Haotong Lin, Sida Peng, Zhen Xu, Yunzhi Yan, Qing Shuai, Hujun Bao, Xiaowei Zhou

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH ASIA* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="zju3dv/ENeRF" >}}

### Abstract
{{< lead >}}
This paper aims to tackle the challenge of efficiently producing interactive free-viewpoint videos. Some recent works equip neural radiance fields with image encoders, enabling them to generalize across scenes. When processing dynamic scenes, they can simply treat each video frame as an individual scene and perform novel view synthesis to generate free-viewpoint videos. However, their rendering process is slow and cannot support interactive applications. A major factor is that they sample lots of points in empty space when inferring radiance fields. We propose a novel scene representation, called ENeRF, for the fast creation of interactive free-viewpoint videos. Specifically, given multi-view images at one frame, we first build the cascade cost volume to predict the coarse geometry of the scene. The coarse geometry allows us to sample few points near the scene surface, thereby significantly improving the rendering speed. This process is fully differentiable, enabling us to jointly learn the depth prediction and radiance field networks from RGB images. Experiments on multiple benchmarks show that our approach exhibits competitive performance while being at least 60 times faster than previous generalizable radiance field methods.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2112.01517" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="ENeRF overview"
    caption="`ENeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="15h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="finetune" message="10mins--2h" color="informational" logo="link" >}}
{{<badge label="render" message="40ms" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="RTX3090" color="informational" logo="link" >}}