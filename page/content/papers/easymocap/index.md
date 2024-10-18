---
date: 2024-10-12T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: EasyMoCap
categories: ["papers"]
tags: ["nerf", "smpl", "multiperson", "siggraph22"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "Novel View Synthesis of Human Interactions from Sparse Multi-view Videos"
summary: TODO
keywords: #
type: '2022' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2022"]
series_order: 13
---

## Novel View Synthesis of Human Interactions from Sparse Multi-view Videos

> Qing Shuai, Chen Geng, Qi Fang, Sida Peng, Wenhao Shen, Xiaowei Zhou, Hujun Bao

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *SIGGRAPH* 2021 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="zju3dv/EasyMocap" >}}

### Abstract
{{< lead >}}
This paper presents a novel system for generating free-viewpoint videos of multiple human performers from very sparse RGB cameras. The system reconstructs a layered neural representation of the dynamic multi-person scene from multi-view videos with each layer representing a moving instance or static background. Unlike previous work that requires instance segmentation as input, a novel approach is proposed to decompose the multi-person scene into layers and reconstruct neural representations for each layer in a weakly-supervised manner, yielding both high-quality novel view rendering and accurate instance masks. Camera synchronization error is also addressed in the proposed approach. The experiments demonstrate the better view synthesis quality of the proposed system compared to previous ones and the capability of producing an editable free-viewpoint video of a real soccer game using several asynchronous GoPro cameras
{{< /lead >}}

{{< button href="https://dl.acm.org/doi/abs/10.1145/3528233.3530704" target="_blank" >}}
Paper
{{< /button >}}