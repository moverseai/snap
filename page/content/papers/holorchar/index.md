---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: HoloChar 
categories: ["papers"]
tags: ["skeleton", "texture", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Holoported Characters: Real-time Free-viewpoint Rendering of Humans from Sparse RGB Cameras"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 44
---

## Holoported Characters: Real-time Free-viewpoint Rendering of Humans from Sparse RGB Cameras

> Ashwath Shetty, Marc Habermann, Guoxing Sun, Diogo Luvizon, Vladislav Golyanik, Christian Theobalt

{{< keywordList >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="ashwath98/deepcharacters" >}}

### Abstract
{{< lead >}}
We present the first approach to render highly realistic free-viewpoint videos of a human actor in general apparel, from sparse multi-view recording to display, in real-time at an unprecedented 4K resolution. At inference, our method only requires four camera views of the moving actor and the respective 3D skeletal pose. It handles actors in wide clothing, and reproduces even fine-scale dynamic detail, e.g. clothing wrinkles, face expressions, and hand gestures. At training time, our learning-based approach expects dense multi-view video and a rigged static surface scan of the actor. Our method comprises three main stages. Stage 1 is a skeleton-driven neural approach for high-quality capture of the detailed dynamic mesh geometry. Stage 2 is a novel solution to create a view-dependent texture using four test-time camera views as input. Finally, stage 3 comprises a new image-based refinement network rendering the final 4K image given the output from the previous stages. Our approach establishes a new benchmark for real-time rendering resolution and quality using sparse input camera views, unlocking possibilities for immersive telepresence.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2312.07423" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="HoloChar teaser"
    caption="`HoloChar` teaser."
    >}}

{{< figure
    src="pipeline.png"
    alt="HoloChar overview"
    caption="`HoloChar` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="DynaCap" color="red" logo="link" link="https://gvv-assets.mpi-inf.mpg.de/" target="_blank">}}
{{<badge label="test" message="HoloChar" color="darkblue" logo="github" link="https://vcai.mpi-inf.mpg.de/projects/holochar/" target="_blank">}}

#### Comparisons
{{<badge label="skeleton--NeRF" message="HDHumans" color="cyan" logo="link" target="_blank">}}
{{<badge label="body--NeRF" message="ENeRF" color="lightcoral" logo="github" link="https://github.com/zju3dv/ENeRF" target="_blank">}}
{{<badge label="body--Splats" message="DVA" color="gainsboro" logo="github" link="https://github.com/facebookresearch/dva" target="_blank">}}



#### Performance
{{<badge label="render" message="40ms" color="informational" logo="link" >}}
{{<badge label="render" message="2_x_A100" color="informational" logo="link" >}}
