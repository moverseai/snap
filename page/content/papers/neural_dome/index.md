---
date: 2023-06-20T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NeuralDome
categories: ["papers"]
tags: ["nerf", "smpl", "cvpr23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
showHero: true
description: "NeuralDome: A Neural Modeling Pipeline on Multi-View Human-Object Interactions"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 16
---

## `NeuralDome`: A Neural Modeling Pipeline on Multi-View Human-Object Interactions

> Juze Zhang, Haimin Luo1, Hongdi Yang, Xinru Xu, Qianyang Wu, Ye Shi, Jingyi Yu, Lan Xu, Jingya Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="email" >}} *CVPR* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="Juzezhang/NeuralDome_Toolbox" >}}

### Abstract
{{< lead >}}
Humans constantly interact with objects in daily life tasks. Capturing such processes and subsequently conducting visual inferences from a fixed viewpoint suffers from occlusions, shape and texture ambiguities, motions, etc. To mitigate the problem, it is essential to build a training dataset that captures free-viewpoint interactions. We construct a dense multi-view dome to acquire a complex human object interaction dataset, named HODome, that consists of ∼71M frames on 10 subjects interacting with 23 objects. To process the HODome dataset, we develop NeuralDome, a layer-wise neural processing pipeline tailored for multi-view video inputs to conduct accurate tracking, geometry reconstruction and free-view rendering, for both human subjects and objects. Extensive experiments on the HODome dataset demonstrate the effectiveness of NeuralDome on a variety of inference, modeling, and rendering tasks.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/CVPR2023/papers/Zhang_NeuralDome_A_Neural_Modeling_Pipeline_on_Multi-View_Human-Object_Interactions_CVPR_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="Neural Dome overview"
    caption="`Neural Dome` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="HODome" color="orange" logo="google" logoColor="white" link="https://drive.google.com/drive/folders/1-QHvcwa71Wk7rdfnQrOyInqK-SWK6lRA" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="ST--NeRF" color="violet" logo="github" link="DarlingHang/ST-NeRF" target="_blank">}}

#### Performance
{{<badge label="train" message="8--10h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3090" color="informational" logo="link" >}}
