---
date: 2022-06-21T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HumanNeRF-1
categories: ["papers"]
tags: ["nerf", "smpl", "cvpr22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "HumanNeRF: Free-viewpoint Rendering of Moving People from Monocular Video"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 1
---

## `HumanNeRF`: Free-viewpoint Rendering of Moving People from Monocular Video

> Chung-Yi Weng, Brian Curless, Pratul P. Srinivasan, Jonathan T. Barron, Ira Kemelmacher-Shlizerman

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="chungyiweng/HumanNeRF" >}}

### Abstract
{{< lead >}}
We introduce a free-viewpoint rendering method – HumanNeRF – that works on a given monocular video of a human performing complex body motions, e.g. a video from YouTube. Our method enables pausing the video at any frame and rendering the subject from arbitrary new camera viewpoints or even a full 360-degree camera path for that particular frame and body pose. This task is particularly challenging, as it requires synthesizing photorealistic details of the body, as seen from various camera angles that may not exist in the input video, as well as synthesizing fine details such as cloth folds and facial appearance. Our method optimizes for a volumetric representation of the person in a canonical T-pose, in concert with a motion field that maps the estimated canonical representation to every frame of the video via backward warps. The motion field is decomposed into skeletal rigid and non-rigid motions, produced by deep networks. We show significant performance improvements over prior work, and compelling examples of free-viewpoint renderings from monocular video of moving humans in challenging uncontrolled capture scenarios
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2201.04127" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="HumanNeRF overview"
    caption="`HumaNeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}

#### Performance
{{<badge label="train" message="72h" color="informational" logo="link" >}}
{{<badge label="train" message="4_x_2080_Ti" color="informational" logo="link" >}}