---
date: 2023-10-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: RelightHuman
categories: ["papers"]
tags: ["nerf", "skeleton", "relight", "monocular", "iccv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "Neural Reconstruction of Relightable Human Model from Monocular Video"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 20
---

## `RelightHuman`: Neural Reconstruction of Relightable Human Model from Monocular Video

> Wenzhang Sun, Yunlong Che, Han Huang, Yandong Guo

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} Skeleton {{< /keyword >}}
{{< keyword icon="tag" >}} Relight {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="sunwenzhang1996/RelightHuman" >}}

### Abstract
{{< lead >}}
Creating relightable and animatable human characters from monocular video at a low cost is a critical task for digital human modeling and virtual reality applications. This task is complex due to intricate articulation motion, a wide range of ambient lighting conditions, and pose-dependent clothing deformations. In this paper, we introduce a novel self-supervised framework that takes a monocular video of a moving human as input and generates a 3D neural representation capable of being rendered with novel poses under arbitrary lighting conditions. Our framework decomposes dynamic humans under varying illumination into neural fields in canonical space, taking into account geometry and spatially varying BRDF material properties. Additionally, we introduce pose-driven deformation fields, enabling bidirectional mapping between canonical space and observation. Leveraging the proposed appearance decomposition and deformation fields, our framework learns in a selfsupervised manner. Ultimately, based on pose-driven deformation, recovered appearance, and physically-based rendering, the reconstructed human figure becomes relightable and can be explicitly driven by novel poses. We demonstrate significant performance improvements over previous works and provide compelling examples of relighting from monocular videos of moving humans in challenging, uncontrolled capture scenarios.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/ICCV2023/papers/Sun_Neural_Reconstruction_of_Relightable_Human_Model_from_Monocular_Video_ICCV_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="RelightHuman overview"
    caption="`RelightHuman` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="Relighting4D" color="yellow" logo="github" link="FrozenBurning/Relighting4D" target="_blank">}}