---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: AnimatableNeRF
categories: ["papers"]
tags: ["nerf", "smpl", "iccv21", "tpami24"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: Animatable Neural Radiance Fields for Modeling Dynamic Human Bodies
summary: TODO
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 3
---

## `AnimatableNeRF`: Animatable Neural Radiance Fields for Modeling Dynamic Human Bodies

> Sida Peng, Junting Dong, Qianqian Wang, Shangzhan Zhang, Qing Shuai, Xiaowei Zhou, Hujun Bao

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2021 {{< /keyword >}}
{{< keyword icon="email" >}} *TPAMI* 2024 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="zju3dv/animatable_nerf" >}}

### Abstract
{{< lead >}}
This paper addresses the challenge of reconstructing an animatable human model from a multi-view video. Some recent works have proposed to decompose a non-rigidly deforming scene into a canonical neural radiance field and a set of deformation fields that map observation-space points to the canonical space, thereby enabling them to learn the dynamic scene from images. However, they represent the deformation field as translational vector field or SE(3) field, which makes the optimization highly under-constrained. Moreover, these representations cannot be explicitly controlled by input motions. Instead, we introduce neural blend weight fields to produce the deformation fields. Based on the skeleton-driven deformation, blend weight fields are used with 3D human skeletons to generate observation-tocanonical and canonical-to-observation correspondences. Since 3D human skeletons are more observable, they can regularize the learning of deformation fields. Moreover, the learned blend weight fields can be combined with input skeletal motions to generate new deformation fields to animate the human model. Experiments show that our approach significantly outperforms recent human synthesis methods. 
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2105.02872" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="AnimatableNeRF overview"
    caption="`AnimatableNeRF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Performance
{{<badge label="train" message="12h" color="informational" logo="link" >}}
{{<badge label="train" message="4_x_2080_Ti" color="informational" logo="link" >}}
{{<badge label="render" message="1sec" color="informational" logo="link" >}}
{{<badge label="render" message="512_x_512" color="informational" logo="link" >}}
{{<badge label="render" message="1080_Ti" color="informational" logo="link" >}}