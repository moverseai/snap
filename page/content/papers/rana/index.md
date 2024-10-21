---
date: 2023-10-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: RANA
categories: ["papers"]
tags: ["nerf", "smpl", "texture", "relight", "monocular", "iccv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "RANA: Relightable Articulated Neural Avatars"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 13
---

## `RANA`: Relightable Articulated Neural Avatars

> Umar Iqbalm, Akin Caliskan, Koki Nagano, Sameh Khamis, Pavlo Molchanov, Jan Kautz

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Relight {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2023 {{< /keyword >}}
{{< /keywordList >}}

### Abstract
{{< lead >}}
We propose RANA, a relightable and articulated neural avatar for the synthesis of humans under arbitrary viewpoints, body poses, and lighting. We only require a short video clip of the person to create the avatar and assume no knowledge about the lighting environment. We present a novel framework to model humans while disentangling their geometry, texture, and lighting environment from monocular RGB videos. To simplify this otherwise ill-posed task we first estimate the coarse geometry and texture of the person via SMPL+D model fitting and then learn an articulated neural representation for higher quality image synthesis. RANA first generates the normal and albedo maps of the person in any given target body pose and then uses spherical harmonics lighting to generate the shaded image in the target lighting environment. We also propose to pre-train RANA using synthetic images and demonstrate that it leads to better disentanglement between geometry and texture while also improving robustness to novel body poses. Finally, we also present a new photo-realistic synthetic dataset, Relighting Human, to quantitatively evaluate the performance of the proposed approach.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/ICCV2023/papers/Iqbal_RANA_Relightable_Articulated_Neural_Avatars_ICCV_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="RANA overview"
    caption="`RANA` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="Relighting4D" color="yellow" logo="github" link="FrozenBurning/Relighting4D" target="_blank">}}