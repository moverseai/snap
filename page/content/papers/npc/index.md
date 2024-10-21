---
date: 2023-10-02T04:14:54-08:00
draft: false
params:
  author: Nikolaos Zioulis
title: NPC
categories: ["papers"]
tags: ["nerf", "smpl", "monocular", "iccv23"]
layout: simple
menu: #
robots: all
# sharingLinks: #
weight: 10
# showPagination: true
# showHero: true
# layoutBackgroundBlur: true
# heroStyle: thumbAndBackground
description: "NPC: Neural Point Characters from Video"
summary: TODO
keywords: #
type: '2023' # we use year as a type to list papers in the list view
series: ["Papers Published @ 2023"]
series_order: 14
---

## `NPC`: Neural Point Characters from Video

> Shih-Yang Su, Timur Bagautdinov, Helge Rhodin

{{< keywordList >}}
{{< keyword icon="tag" >}} NeRF {{< /keyword >}}
{{< keyword icon="tag" >}} SMPL {{< /keyword >}}
{{< keyword icon="tag" >}} Monocular {{< /keyword >}}
{{< keyword icon="email" >}} *ICCV* 2023 {{< /keyword >}}
{{< /keywordList >}}

{{< github repo="LemonATsu/NPC-pytorch" >}}

### Abstract
{{< lead >}}
High-fidelity human 3D models can now be learned directly from videos, typically by combining a template-based surface model with neural representations. However, obtaining a template surface requires expensive multi-view capture systems, laser scans, or strictly controlled conditions. Previous methods avoid using a template but rely on a costly or ill-posed mapping from observation to canonical space. We propose a hybrid point-based representation for reconstructing animatable characters that does not require an explicit surface model, while being generalizable to novel poses. For a given video, our method automatically produces an explicit set of 3D points representing approximate canonical geometry, and learns an articulated deformation model that produces pose-dependent point transformations. The points serve both as a scaffold for high-frequency neural features and an anchor for efficiently mapping between observation and canonical space. We demonstrate on established benchmarks that our representation overcomes limitations of prior work operating in either canonical or in observation space. Moreover, our automatic point extraction approach enables learning models of human and animal characters alike, matching the performance of the methods using rigged surface templates despite being more general.
{{< /lead >}}

{{< button href="https://openaccess.thecvf.com/content/ICCV2023/papers/Su_NPC_Neural_Point_Characters_from_Video_ICCV_2023_paper.pdf" target="_blank" >}}
Paper
{{< /button >}}

### Approach

{{< figure
    src="overview.png"
    alt="NPC overview"
    caption="`NPC` overview."
    >}}

### Results

#### Data
{{<badge label="test" message="ZJU_MOCAP" color="yellowgreen" logo="github" link="https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset" target="_blank">}}
{{<badge label="test" message="Human3.6M" color="critical" logo="link" link="http://vision.imar.ro/human3.6m/description.php" target="_blank">}}

#### Comparisons
{{<badge label="body--NeRF" message="NeuralBody" color="coral" logo="github" link="https://github.com/zju3dv/neuralbody" target="_blank">}}
{{<badge label="body--NeRF" message="AnimatableNeRF" color="cyan" logo="github" link="https://github.com/zju3dv/animatable_nerf" target="_blank">}}
{{<badge label="body--NeRF" message="TAVA" color="coral" logo="github" link="facebookresearch/tava" target="_blank">}}
{{<badge label="body--NeRF" message="ARAH" color="magenta" logo="github" link="https://github.com/taconite/arah-release" target="_blank">}}
{{<badge label="body--NeRF" message="DANBO" color="pink" logo="github" link="LemonATsu/DANBO-pytorch" target="_blank">}}

#### Performance
{{<badge label="train" message="12h" color="informational" logo="link" >}}
{{<badge label="train" message="RTX3080" color="informational" logo="link" >}}
{{<badge label="render" message="1000_x_1000" color="informational" logo="link" >}}
{{<badge label="render" message="V100" color="informational" logo="link" >}}
{{<badge label="render" message="7sec" color="informational" logo="link" >}}