---
date: 2023-10-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SurMo
categories: ["papers"]
tags: ["nerf", "smpl", "texture", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "SurMo: Surface-based 4D Motion Modeling for Dynamic Human Rendering"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 30
---

## `SurMo`: Surface-based 4D Motion Modeling for Dynamic Human Rendering

> Tao Hu, Fangzhou Hong, Ziwei Liu

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="TaoHuUMD/SurMo" >}}

### Abstract
{{< lead >}}
Dynamic human rendering from video sequences has achieved remarkable progress by formulating the rendering as a mapping from static poses to human images. However, existing methods focus on the human appearance reconstruction of every single frame while the temporal motion relations are not fully explored. In this paper, we propose a new 4D motion modeling paradigm, SurMo, that jointly models the temporal dynamics and human appearances in a unified framework with three key designs: 1) Surface-based motion encoding that models 4D human motions with an efficient compact surface-based triplane. It encodes both spatial and temporal motion relations on the dense surface manifold of a statistical body template, which inherits body topology priors for generalizable novel view synthesis with sparse training observations. 2) Physical motion decoding that is designed to encourage physical motion learning by decoding the motion triplane features at timestep t to predict both spatial derivatives and temporal derivatives at the next timestep t+1 in the training stage. 3) 4D appearance decoding that renders the motion triplanes into images by an efficient volumetric surface-conditioned renderer that focuses on the rendering of body surfaces with motion learning conditioning. Extensive experiments validate the state-of-the-art performance of our new paradigm and illustrate the expressiveness of surface-based motion triplanes for rendering high-fidelity view-consistent humans with fast motions and even motion-dependent shadows.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2024/papers/Hu_SurMo_Surface-based_4D_Motion_Modeling_for_Dynamic_Human_Rendering_CVPR_2024_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="SurMo teaser"
    caption="`SurMo` teaser."
    >}}

{{< figure
    src="method.png"
    alt="SurMo overview"
    caption="`SurMo` overview."
    >}}


### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="AIST++" color="navy" logo="github" link="https://google.github.io/aistplusplus_dataset/factsfigures.html" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="InstantNVR" color="fuchsia" logo="github" link="https://github.com/zju3dv/instant-nvr" target="_blank">}}
{{<badge label="body--NeRF" message="HumanNeRF" color="blue" logo="github" link="chungyiweng/HumanNeRF" target="_blank">}}