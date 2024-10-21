---
date: 2022-12-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SCARF
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "clothing", "siggraph_asia22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "Capturing and Animation of Body and Clothing from Monocular Video"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 27
---

## `SCARF`: Capturing and Animation of Body and Clothing from Monocular Video

> Yao Feng, Jinlong Yang, Marc Pollefeys, Michael J. Black, Timo Bolkart

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL  {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="tag" >}} Clothing {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH Asia* 2022 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="yfeng95/SCARF" >}}

### Abstract
{{< lead >}}
While recent work has shown progress on extracting clothed 3D human avatars from a single image, video, or a set of 3D scans, several limitations remain. Most methods use a holistic representation to jointly model the body and clothing, which means that the clothing and body cannot be separated for applications like virtual try-on. Other methods separately model the body and clothing, but they require training from a large set of 3D clothed human meshes obtained from 3D/4D scanners or physics simulations. Our insight is that the body and clothing have different modeling requirements. While the body is well represented by a mesh-based parametric 3D model, implicit representations and neural radiance fields are better suited to capturing the large variety in shape and appearance present in clothing. Building on this insight, we propose SCARF (Segmented Clothed Avatar Radiance Field), a hybrid model combining a mesh-based body with a neural radiance field. Integrating the mesh into the volumetric rendering in combination with a differentiable rasterizer enables us to optimize SCARF directly from monocular videos, without any 3D supervision. The hybrid modeling enables SCARF to (i) animate the clothed body avatar by changing body poses (including hand articulation and facial expressions), (ii) synthesize novel views of the avatar, and (iii) transfer clothing between avatars in virtual try-on applications. We demonstrate that SCARF reconstructs clothing with higher visual quality than existing methods, that the clothing deforms with changing body pose and body shape, and that clothing can be successfully transferred between avatars of different subjects.
{{< /lead >}}

{{< button href="https://dl.acm.org/doi/pdf/10.1145/3550469.3555423" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="SCARF overview"
    caption="`SCARF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="Anim--NeRF" color="yellow" logo="github" link="https://github.com/JanaldoChen/Anim-NeRF" target="_blank">}}

#### Performance
{{<badge label="train" message="40h" color="informational" logo="link" >}}
{{<badge label="train" message="V100" color="informational" logo="link" >}}