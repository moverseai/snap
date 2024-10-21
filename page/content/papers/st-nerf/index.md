---
date: 2021-08-01T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: ST-NeRF
categories: ["papers"]
tags: ["nerf", "siggraph21"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Editable Free-Viewpoint Video using a Layered Neural Representation"
summary: TODO
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 9
---

## `ST-NeRF`: Editable Free-Viewpoint Video using a Layered Neural Representation


> Jiakai Zhang, Xinhang Liu, Xinyi Ye, Fuqiang Zhao, Yanshun Zhang, Minye Wu, Yingliang Zhang, Lan Xu, Jingyi Yu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Deformation {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH* 2021 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="DarlingHang/ST-NeRF" >}}

### Abstract
{{< lead >}}
Generating free-viewpoint videos is critical for immersive VR/AR experience, but recent neural advances still lack the editing ability to manipulate the visual perception for large dynamic scenes. To fill this gap, in this paper, we propose the first approach for editable free-viewpoint video generation for large-scale view-dependent dynamic scenes using only 16 cameras. The core of our approach is a new layered neural representation, where each dynamic entity, including the environment itself, is formulated into a spatiotemporal coherent neural layered radiance representation called ST-NeRF. Such a layered representation supports manipulations of the dynamic scene while still supporting a wide free viewing experience. In our ST-NeRF, we represent the dynamic entity/layer as a continuous function, which achieves the disentanglement of location, deformation as well as the appearance of the dynamic entity in a continuous and self-supervised manner. We propose a scene parsing 4D label map tracking to disentangle the spatial information explicitly and a continuous deform module to disentangle the temporal motion implicitly. An object-aware volume rendering scheme is further introduced for the re-assembling of all the neural layers. We adopt a novel layered loss and motion-aware ray sampling strategy to enable efficient training for a large dynamic scene with multiple performers, Our framework further enables a variety of editing functions, i.e., manipulating the scale and location, duplicating or retiming individual neural layers to create numerous visual effects while preserving high realism. Extensive experiments demonstrate the effectiveness of our approach to achieve high-quality, photo-realistic, and editable free-viewpoint video generation for dynamic scenes
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2104.14786" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="ST-NeRF overview"
    caption="`ST-NeRF` overview."
    >}}

### Results

#### Performance
{{<badge label="train" message="12--36h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="train" message="960_×_540" color="informational" logo="link" >}}
{{<badge label="finetune" message="2--3d" color="informational" logo="link" >}}
{{<badge label="finetune" message="1920_×_1080" color="informational" logo="link" >}}
{{<badge label="render" message="1920_×_1080" color="informational" logo="link" >}}
{{<badge label="render" message="2mins" color="informational" logo="link" >}}