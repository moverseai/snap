---
date: 2024-06-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: GHNeRF
categories: ["papers"]
tags: ["nerf", "generalized", "cvpr24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "GHNeRF: Learning Generalizable Human Features with Efficient Neural Radiance Fields"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 10
---

## `GHNeRF`: Learning Generalizable Human Features with Efficient Neural Radiance Fields

> Arnab Dey, Di Yang, Rohith Agaram, Antitza Dantcheva, Andrew I. Comport, Srinath Sridhar, Jean Martinet

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2024 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
Recent advances in Neural Radiance Fields (NeRF) have demonstrated promising results in 3D scene representa- tions, including 3D human representations. However, these representations often lack crucial information on the un- derlying human pose and structure, which is crucial for AR/VR applications and games. In this paper, we intro- duce a novel approach, termed GHNeRF, designed to ad- dress these limitations by learning 2D/3D joint locations of human subjects with NeRF representation. GHNeRF uses a pre-trained 2D encoder streamlined to extract essential human features from 2D images, which are then incorpo- rated into the NeRF framework in order to encode human biomechanic features. This allows our network to simulta- neously learn biomechanic features, such as joint locations, along with human geometry and texture. To assess the effec- tiveness of our method, we conduct a comprehensive com- parison with state-of-the-art human NeRF techniques and joint estimation algorithms. Our results show that GHNeRF can achieve state-of-the-art results in near real-time.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2024W/NRI/papers/Dey_GHNeRF_Learning_Generalizable_Human_Features_with_Efficient_Neural_Radiance_Fields_CVPRW_2024_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="GHNeRF overview"
    caption="`GHNeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="ENeRF" color="lightcoral" logo="github" link="https://github.com/zju3dv/ENeRF" target="_blank">}}
{{<badge label="body--NeRF" message="SHERF" color="mediumblue" logo="github" link="https://github.com/skhu101/SHERF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}

#### Performance
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="89ms" color="informational" logo="link" >}}