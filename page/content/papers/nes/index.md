---
date: 2023-08-29T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NES
categories: ["papers"]
tags: ["nerf", "smpl", "sdf", "acmmm23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Explicifying Neural Implicit Fields for Efficient Dynamic Human Avatar Modeling via a Neural Explicit Surface"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 10
---

## `NES`: Explicifying Neural Implicit Fields for Efficient Dynamic Human Avatar Modeling via a Neural Explicit Surface

> Ruiqi Zhang, Jie Chen, Qiang Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} SDF {{< /keyword >}}
{{< keyword icon="email" >}} *ACM Multimedia* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
This paper proposes a technique for efficiently modeling dynamic humans by explicifying the implicit neural fields via a Neural Explicit Surface (NES). Implicit neural fields have advantages over traditional explicit representations in modeling dynamic 3D content from sparse observations and effectively representing complex geometries and appearances. Implicit neural fields defined in 3D space, however, are expensive to render due to the need for dense sampling during volumetric rendering. Moreover, their memory efficiency can be further optimized when modeling sparse 3D space. To overcome these issues, the paper proposes utilizing Neural Explicit Surface (NES) to explicitly represent implicit neural fields, facilitating memory and computational efficiency. To achieve this, the paper creates a fully differentiable conversion between the implicit neural fields and the explicit rendering interface of NES, leveraging the strengths of both implicit and explicit approaches. This conversion enables effective training of the hybrid representation using implicit methods and efficient rendering by integrating the explicit rendering interface with a newly proposed rasterizationbased neural renderer that only incurs a texture color query once for the initial ray interaction with the explicit surface, resulting in improved inference efficiency. NES describes dynamic human geometries with pose-dependent neural implicit surface deformation fields and their dynamic neural textures both in 2D space, which is a more memory-efficient alternative to traditional 3D methods, reducing redundancy and computational load. The comprehensive experiments show that NES performs similarly to previous 3D approaches, with greatly improved rendering speed and reduced memory cost.
{{< /lead >}}

{{< button href="https://dl.acm.org/doi/pdf/10.1145/3581783.3611707?casa_token=eambQQ4cbgcAAAAA:3Q9hDQLgh4jEtXpIIzKPJ8rghqdbXSHr1IBr06lPj3SwSkNzHn7Y_efGdymW18D-cfJVghuoa8Z0hA" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="NES overview"
    caption="`NES` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="SANeRF" color="teal" logo="github" link="https://github.com/pfnet-research/surface-aligned-nerf" target="_blank">}}

#### Performance
{{<badge label="render" message="60ms" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="2_x_A100" color="informational" logo="link" >}}