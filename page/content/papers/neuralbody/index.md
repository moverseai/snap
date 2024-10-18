---
date: 2021-06-19T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NeuralBody
categories: ["papers"]
tags: ["nerf", "smpl", "cvpr21", "tpami23"]
layout: simple # single # 
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Neural Body: Implicit Neural Representations with Structured Latent Codes for Novel View Synthesis of Dynamic Humans"
summary: TODO
keywords: #
type: '2021' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2021"]
series_order: 8
---

## `NeuralBody`: Implicit Neural Representations with Structured Latent Codes for Novel View Synthesis of Dynamic Humans

> Sida Peng, Yuanqing Zhang, Yinghao Xu, Qianqian Wang, Qing Shuai, Hujun Bao, Xiaowei Zhou

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2021 {{< /keyword >}}
{{< keyword icon="email" >}} *TPAMI* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="zju3dv/neuralbody" >}}

### Abstract
{{< lead >}}
This paper addresses the challenge of novel view synthesis for a human performer from a very sparse set of camera views. Some recent works have shown that learning implicit neural representations of 3D scenes achieves remarkable view synthesis quality given dense input views. However, the representation learning will be ill-posed if the views are highly sparse. To solve this ill-posed problem, our key idea is to integrate observations over video frames. To this end, we propose Neural Body, a new human body representation which assumes that the learned neural representations at different frames share the same set of latent codes anchored to a deformable mesh, so that the observations across frames can be naturally integrated. The deformable mesh also provides geometric guidance for the network to learn 3D representations more efficiently. To evaluate our approach, we create a multi-view dataset named ZJU-MoCap that captures performers with complex motions. Experiments on ZJU-MoCap show that our approach outperforms prior works by a large margin in terms of novel view synthesis quality. We also demonstrate the capability of our approach to reconstruct a moving person from a monocular video on the People-Snapshot dataset. 
{{< /lead >}}

{{< button href="https://arxiv.org/pdf/2012.15838v2" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="method.jpg"
    alt="Neural Body overview"
    caption="`Neural Body` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="PeopleSnapshot" color="lightblue" logo="link" link="https://graphics.tu-bs.de/people-snapshot" target="_blank">}}
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}


#### Performance
{{<badge label="train" message="14h" color="informational" logo="link" >}}
{{<badge label="train" message="4_x_2080_Ti" color="informational" logo="link" >}}
