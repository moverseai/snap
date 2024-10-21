---
date: 2023-10-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: SHERF
categories: ["papers"]
tags: ["nerf", "smpl", "generalized", "monocular", "iccv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "SHERF: Generalizable Human NeRF from a Single Image"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 18
---

## `SHERF`: Generalizable Human NeRF from a Single Image

> Jiteng Mu, Shen Sang, Nuno Vasconcelos, Xiaolong Wang

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Generalized {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="skhu101/SHERF" >}}

### Abstract
{{< lead >}}
Existing Human NeRF methods for reconstructing 3D humans typically rely on multiple 2D images from multi-view cameras or monocular videos captured from fixed camera views. However, in real-world scenarios, human images are often captured from random camera angles, presenting
challenges for high-quality 3D human reconstruction. In this paper, we propose SHERF, the first generalizable Human NeRF model for recovering animatable 3D humans from a single input image. SHERF extracts and encodes 3D human representations in canonical space, enabling rendering and animation from free views and poses. To achieve high-fidelity novel view and pose synthesis, the encoded 3D human representations should capture both global appearance and local fine-grained textures. To this end, we propose a bank of 3D-aware hierarchical features, including global, point-level, and pixel-aligned features, to facilitate informative encoding.Global features enhance the information extracted from the single input image and complement the information missing from the partial 2D observation. Point-level features provide strong clues of 3D human structure, while pixel-aligned features preserve more fine-grained details. To effectively integrate the 3D-aware hierarchical feature bank, we design a feature fusion transformer. Extensive experiments on THuman, RenderPeople, ZJU_MoCap, and HuMMan datasets demonstrate that SHERF achieves state-of-the-art performance, with better generalizability for novel view and pose synthesis
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/ICCV2023/papers/Hu_SHERF_Generalizable_Human_NeRF_from_a_Single_Image_ICCV_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="SHERF overview"
    caption="`SHERF` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="RenderPeople" color="magenta" style="plastic" logo="link" link="https://renderpeople.com/free-3d-people/" target="_blank">}}
{{<badge label="test" message="THuman" color="orange" style="plastic" logo="github" link="https://github.com/ZhengZerong/DeepHuman/tree/master/THUmanDataset" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="MPS-NeRF" color="gold" logo="github" link="gaoxiangjun/MPS-NeRF" target="_blank">}}
{{<badge label="body--NeRF" message="NeuralHumanPerformer" color="lime" logo="github" link="https://github.com/YoungJoongUNC/Neural_Human_Performer" target="_blank">}}