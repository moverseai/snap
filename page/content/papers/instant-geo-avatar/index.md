---
date: 2024-12-06T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: InstantGeoAvatar
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "texture", "accv24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "InstantGeoAvatar: Effective Geometry and Appearance Modeling of Animatable Avatars from Monocular Video"
summary: TODO
keywords: #
type: '2024' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2024"]
series_order: 29
---

## `InstantGeoAvatar`: Effective Geometry and Appearance Modeling of Animatable Avatars from Monocular Video

> Alvaro Budria, Adrian Lopez-Rodriguez, Òscar Lorente, and Francesc Moreno-Noguer

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Texture {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ACCV* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="alvaro-budria/InstantGeoAvatar" >}}

### Abstract
{{< lead >}}
We present InstantGeoAvatar, a method for efficient and effective learning from monocular video of detailed 3D geometry and appearance of animatable implicit human avatars. Our key observation is that the optimization of a hash grid encoding to represent a signed distance function (SDF) of the human subject is fraught with instabilities and bad local minima. We thus propose a principled geometry-aware SDF regularization scheme that seamlessly fits into the volume rendering pipeline and adds negligible computational overhead. Our regularization scheme significantly outperforms previous approaches for training SDFs on hash grids. We obtain competitive results in geometry reconstruction and novel view synthesis in as little as five minutes of training time, a significant reduction from the several hours required by previous work. InstantGeoAvatar represents a significant leap forward towards achieving interactive reconstruction of virtual avatars.
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2411.01512" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="teaser.png"
    alt="Paper teaser"
    caption="Paper teaser."
    >}}

{{< figure
    src="method.png"
    alt="Method overview"
    caption="Method overview."
    >}}


### Results

#### Data
{{<badge label="test" message="X--Humans" color="goldenrod" logo="github" link="https://xhumans.ait.ethz.ch/" target="_blank">}}
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="Vid2Avatar" color="palegreen" logo="github" link="https://github.com/MoyGcc/vid2avatar" target="_blank">}}
{{<badge label="body--NeRF" message="InstantAvatar" color="violet" logo="github" link="https://github.com/tijiang13/InstantAvatar" target="_blank">}}
