---
title: Solving Neural Articulated Performances
date: 2025-02-10
draft: false
logo_path: 
website: 
description: Solving Neural Articulated Performances. Animatable human digital representations consolidate human reconstruction and simulation. They can jointly serve as the technical backbone for holistic performance capture, rich 3D human assets and efficient tele-presence. SNAP is a project that seeks to explore the synergies between human motion capture and appearance reconstruction as enabled by the neural graphics and vision continuum.
layout: article # simple # single # article
showAuthor: false
showZenMode: true
# tags: []
authors:
  - "nick"
---

<!-- # ***S***olving ***N***eural ***A***rticulated ***P***erformances -->


<!-- ## ***D***ynamic ***H***uman ***P***erformances -->
<!-- ## **D**ynamic **H**uman **P**erformances -->
## Dynamic Human Performances

{{< lead >}}
> a digitization challenge
{{< /lead >}}

Humans move in distinctly varying ways depending on the context and surrounding environment. 
Human motion exploits and engages with the `space` around us to convey thoughts and emotions, perform actions, play instruments or express intentions.
`Body motion` is the common denominator to all these activities. 
Our motions mix coarse limb motion, fine grained finger manipulation, and facial expressions. 

<!-- ![](img/ahmad-odeh-TK_WT3dl2tw-unsplash.jpg "[`Image`](https://unsplash.com/photos/group-of-people-dancing-photo-TK_WT3dl2tw) of a group performance by [`Ahmad Odeh`](https://unsplash.com/@aoddeh)") -->

{{< figure
    src="img/ahmad-odeh-TK_WT3dl2tw-unsplash.jpg"
    alt="Image of a group of performance by Ahmad Odeh"
    caption="[`Image`](https://unsplash.com/photos/group-of-people-dancing-photo-TK_WT3dl2tw) of a group performance by [`Ahmad Odeh`](https://unsplash.com/@aoddeh)" class="centered-image"
>}}

Even though performances vary, our flexibility and adaptability in motion allows us to `fluently transition` from one type of motion (_e.g. sports_) to another (_e.g. dance_). 
We blend and mix motion types, showing emotions while dancing or playing sports. 
This high-dimensional transition space renders human performance capturing and digitization `very challenging`. 
Using objects, clothing and hair in said performances significantly expands capturing complexity.
Additionally considering simultaneous and/or interacting performers, as well as (social) group dynamics, makes the challenge and complexity scale exponentially.
But nowdays we are witnessing another exponential curve, a technological one.

<!-- ## ***N***eural ***G***raphics & ***V***ision -->
## Neural Graphics & Vision

{{< lead >}}
> the new continuum
{{< /lead >}}

`Reconstruction` and `simulation` are the two ends of a digital thread we use to make sense of our physical world. 
On one end, `computer vision` uses sensors to reconstruct our surroundings, whereas, on the other end, `computer graphics` rely on models to simulate them. 
For years, the reconstruction end has lagged behind simulation which has been producing impressive visual effects, virtual worlds and cinematics. 

{{< figure
    src="img/8fb529fa-ccb7-449d-bc85-64dc8cb635ff.jpg"
    alt="A generated image of the digital computer graphics-to-vision continuum." class="centered-image"
>}}

But nowadays, the recent advances in `machine learning` have improved machine perception. 
It is now possible to understand our environments and reconstruct their various layers. 
These span from lower level ones like 3D geometry and appearance to higher level ones, like semantics and even affordances.
Said advances are also affecting the other end, enabling simulation technology that is more efficient.
This works in tandem with the reconstruction progress, creating a `virtuous cycle`.

<!-- ![ngv continuum](img/430a4a82-579d-4b55-945c-d221990c8e90.jpg "the ngv continuum") -->

<!-- ![Generated continuum](img/8fb529fa-ccb7-449d-bc85-64dc8cb635ff.jpg "A `generated` image of the digital computer graphics-to-vision continuum.") -->



<!-- caption="A `generated` image of the digital computer graphics-to-vision continuum."  -->

It used to be that engineers and scientists worked at the intersection of graphics and vision. 
Neural techniques are now `tying the knot`, connecting these two ends. 
As a result, novel techniques are emerging, allowing us to traverse the graphics-to-vision continuum seamlessly, and opening up new pathways to explore.


## Richer Assets

{{< lead >}}
> the real in hyper-realistic
<!-- > with extra layers -->
{{< /lead >}}


High quality character performances are produced for film, visual effects and game cinematics. 
Technologies like animation, deformation and physically-based rendering are the driving forces of such compelling content. 
Still, these need immense human effort - and also, `artistry` - to create, and have been enabled by real-time editing tools, themselves being aggregations of many technical advances. 

<!-- ![](img/astronaut.png "[`Animated 3D Asset`](https://sketchfab.com/3d-models/tripo-astronaut-animated-bf065335fc194bfeac12439b804f6135) by [`Jungle Jim`](https://sketchfab.com/jungle_jim)") -->

{{< figure
    src="img/astronaut.png"
    alt="Animated 3D Asset"
    caption="[`Animated 3D Asset`](https://sketchfab.com/3d-models/tripo-astronaut-animated-bf065335fc194bfeac12439b804f6135) by [`Jungle Jim`](https://sketchfab.com/jungle_jim)" class="centered-image"
>}}

Up to now this has been solely on the simulation side of the continuum. 
It is almost a decade ago that we started reconstructing production-grade human performances. 
Microsoft’s Mixed Reality Capture Studio Technology <cite>[^1]</cite> (now at [Arcturus](https://arcturus.studio/blog/microsoft-partnership/)), [4DViews](https://www.4dviews.com/), [Volucap](https://volucap.com/) and [Volograms](https://www.volograms.com/) delivered impressive 4D capture systems. 

<!-- ![](img/microsoft_mixed_reality_capture_studios.jpg "Microsoft Mixed Reality Capture Studio") -->

{{< figure 
    src="img/microsoft_mixed_reality_capture_studios.jpg"
    alt="Microsoft Mixed Reality Capture Studio"
    caption="Microsoft Mixed Reality Capture Studio" class="centered-image"
    >}}

<!-- {{< twitter user="MSFTVolumetric" id="1304087262406139909" >}} -->

<!-- {{< lead >}} -->
<!-- {{< /lead >}} -->
<!-- While controllability and editing is possible with the right tools for these new 4D formats, more recent advances showcase new potential to extend capture to deformations, thin structures, and even effects not possible before. -->
Still, recent advances exhibit new potential to extend capturing to deformations, thin structures, and even effects not possible before.
The earlier works of 2021<cite>[^2]</cite> and 2022<cite>[^3]</cite> using implicit neural fields achieved human capture with body pose or time dependent `deformations`.

<!-- ### Deformation -->

|     |  |
| :--------: | :-------: |
| {{< list title="2021" cardView=false limit=2 where="Type" value="2021" >}}  | {{< list title="2022" cardView=false limit=2 where="Type" value="2022" >}}   |

<!-- {{< list title="2021" cardView=false limit=3 where="Type" value="2021" >}} -->

<!-- {{< list title="2022" cardView=true limit=3 where="Type" value="2022" >}} -->

Following up, more recent works are starting to reconstruct and simulate complex `cloth`<cite>[^4]</cite> dynamics, as well as `hair` <cite>[^5]</cite>:

<!-- #### Cloth -->

| Cloth    | Hair |
| :--------: | :-------: |
| {{< utube id=MSSDDk5p270 start=20 end=28 loading=lazy allowFullScreen=false autoplay=false controls=false mute=true class=dummy >}}  | {{< linkedin "7264793394663636992" >}}    |

<!-- {{< utube id=MSSDDk5p270 start=20 end=45 loading=lazy allowFullScreen=false autoplay=false controls=false class=dummy >}} -->

<!-- #### Hair -->
<!-- {{< utube id=a-OAWqBzldU start=5 end=12 loading=lazy allowFullScreen=false autoplay=false controls=false class=dummy >}} -->

<!-- {{< linkedin "7264793394663636992" >}} -->

<!-- > Capture by [Eric Paré](https://ericpare.com/) -->

<!-- ### Effects -->

Another new capability emerging from the use of neural rendering and radiance field techniques is the capture of `effects` from participating media. These enable the capture of lighting variations and reflections:

|     |  |
| :--------: | :-------: |
| {{< luma "36783a60-d040-442d-80f3-b8bca256e225" >}}  | {{< luma "90449613-d135-49db-92c9-20e70c2b9672" >}}  |

<!-- {{< luma "36783a60-d040-442d-80f3-b8bca256e225" >}} -->
<!-- 742c4d5a-d2ec-42e0-b234-8ac20079392b -->
<!-- af1032f5-8689-4c56-8ee7-99138833e556 -->
<!-- f36192fd-0379-4152-90dd-cbd59452b57c -->

Further, these techniques can drive the capturing of `subsurface scattering`<cite>[^6]</cite>, `smoke` and `clouds`<cite>[^7]</cite>, or scenes through `fog`<cite>[^8]</cite> and `water`<cite>[^9]</cite>! 

Examples being the capture of volumetric effects such as `fire` {{< icon fire >}} and `lights` {{< icon lightbulb >}}, now possible, as shown by the creative *Gaussian Splatting* works of [Stéphane Couchoud](https://www.youtube.com/@couchoud) and [Eric Paré](https://ericpare.com/) respectively:

| Fire  {{< icon fire >}}  | Lights {{< icon lightbulb >}}  |
| :--------: | :-------: |
| {{< linkedin "7253106220188753922" >}}  | {{< linkedin "7266263013035315200" >}}    |

<!-- {{< linkedin "7253106220188753922" >}} -->

<!-- {{< linkedin "7266263013035315200" >}} -->

<!-- <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7264793394663636992" height="1116" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7266263013035315200" height="583" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe> -->

<!-- ### Scaling Down !  -->

<!-- {{< keyword icon="wand-magic-sparkles" >}} Scale down {{< /keyword >}} -->

Evidently, we are reaching a critical point where the combined progress driven by AI and differentiable rendering will consolidate into human capturing technology that delivers much `richer assets`. 
Assets that disentangle the various appearance, geometry, deformation and animation layers, maximizing editability and control. More importantly, this should be possible while simultaneously `downscaling` the capturing requirements from hundreds of cameras and controlled environments, to portable and/or mobile systems deployed in-the-wild.

<!-- ## ***S***calable ***R***epresentations -->
## ***L***ive ***R***epresentations

{{< lead >}}
<!-- > real-time holograms -->
> holograms, my young Padawan
{{< /lead >}}

`Tele-presence` promises to elevate real-time collaboration and communication beyond contemporary audio-visual systems. 
Considering its digital nature, it has the potential to surpass the “*golden standard*” of face-to-face communication. 
Up to now systems like [Microsoft's Holoportation](https://www.microsoft.com/en-us/research/project/holoportation-3/earlier-work/) and [Google's Starline](https://starline.google/) spearhead tele-presence technology. 
The requirement of `interaction level latency` makes said systems very complex. 
It is a huge pain point as it applies end-to-end, extending beyond capturing to transmission and rendering.
The chosen 3D representation changes the design surface of any real-time telepresence system. 
This includes the capturing setup and upstream `bandwidth`; the capacity and performance of the server and client components for encoding/decoding; rendering, and/or spatial tiling/level-of-detail support. 
All these influence latency and up/downstream bandwidth, as well as the fidelity of the reconstruction and resulting `QoE`.
While research efforts started focusing on new forms of compression<cite>[^10]</cite>, and streamability<cite>[^11]</cite>, animateable radiance field based representations pose as a promising solution to better manage the underlying trade-offs.

{{< utube id=bS4Gf0PWmZs start=7 end=17 loading=lazy allowFullScreen=false autoplay=false controls=false class=dummy >}}

Using such `drivable` representations, streaming lightweight animation data can control a deformable representation.
This alleviates the need to transmit dense visual representations and only pay a one-off cost for the drivable representation.
Compared to contemporary skinned animation, it can also support pose-controlled deformations, conveying the necessary realism.
The video above shows Meta's [Codec Avatars](https://tech.facebook.com/reality-labs/2019/3/codec-avatars-facebook-reality-labs/), a technology that has been focusing on exploring the advantages of real-time avatar drivability<cite>[^12]</cite><cite>,[^13]</cite>.

<!-- Radiance field based representations pose as a solution to better manage the QoS/QoE trade-offs. 
Being relatively new, most ongoing improvements are necessary:

- High quality drivability has been shown to be possible [MetaCodec], as well as,
- improving rendering speed to support heterogeneous devices [rendering speed],
- compressing the representations [spz compression, nerf compression],
- and/or making them streamable [streamable nerf].

A promising direction is animatable radiance fields. Using them, lightweight animation data can control a deformable representation. This allows for efficient transmission, with a one-off cost for the underlying representation. Compared to contemporary skinned animation, it also supports pose-controlled deformations out-of-the-box. -->

## So … ***SNAP***!

{{< lead >}}
> a new way ?
<!-- > a new way of doing old things -->
{{< /lead >}}

Animatable human digital representations consolidate human reconstruction and simulation.
They can jointly serve as the technical backbone for holistic `performance capture`, rich `3D human assets` and efficient `tele-presence`.

`SNAP` is a project that seeks to explore the `synergies` between human motion and appearance capture as enabled by the `neural graphics and vision continuum`.
The tools are numerous, ranging from explicit parametric body models, to implicit fields, differentiable rendering and efficiently optimized gaussian splats.

From an end goal perspective, animatable humans based on `neural fields` and/or `gaussian splats` require high quality `motion capture`.
But once a simulation ready digital `radiance field avatar` of an actor is reconstructed, one that can deform clothing and respect lighting variations as the body moves, or even move hair; then it can also be used to `solve for complex human performances` using solely the raw image data.
Taking into account that markerless motion capture and human radiance field technologies are developed for the same acquisition system - color camera(s) - the `interplay` between these two technologies is significant and worth exploring.

<!-- 
New tech pathways emerge from the evolving and volatile current technological landscape. SNAP grounds itself on the interaction between character animation and view synthesis. Its focus is on exploring one such new pathway, animateable radiance fields. This class of approach relies on high quality motion capture. The latter can improve the radiance fields' initialization and convergence. But the interaction benefits can additionally be bi-directional. The radiance fields can in turn improve the original motion capture [ref].
Considering markerless motion capture, these two adjacent technologies' interplay is significant:
- the input data, posed viewpoints and raw images, coincide, and
- the outputs can synergistically improve each other, as well as,
- interact via pose-controllability/drivability,
  - offering a new form of easily acquired richer assets, or
  - allowing for a new form of streaming 3D media. -->


## References

[^1]:	[High-Quality Streamable Free-Viewpoint Video](https://hhoppe.com/proj/fvv/), SIGGRAPH 2015
[^2]: [Human NeRF papers @ 2021](/snap/papers2021)
[^3]: [Human NeRF papers @ 2022](/snap/papers2022)
[^4]: [Reloo: Reconstructing humans dressed in loose garments from monocular video in the wild](https://moygcc.github.io/ReLoo/), ECCV 2024
[^5]: [NeRSemble: Multi-view Radiance Field Reconstruction of Human Heads](https://tobias-kirschstein.github.io/nersemble/), SIGGRAPH 2023
[^6]: [Subsurface Scattering for 3D Gaussian Splatting](https://sss.jdihlmann.com/), NeurIPS 2024
[^7]: [Don't Splat your Gaussians: Volumetric Ray-Traced Primitives for Modeling and Rendering Scattering and Emissive Media](https://arcanous98.github.io/projectPages/gaussianVolumes.html)
[^8]: [ScatterNeRF: Seeing Through Fog with Physically-Based Inverse Neural Rendering](https://light.princeton.edu/publication/scatternerf/), ICCV 2023
[^9]: [Gaussian Splashing: Direct Volumetric Rendering Underwater](https://bgu-cs-vil.github.io/gaussiansplashingUW.github.io/)
[^10]: [How Far Can We Compress Instant-NGP-Based NeRF?](https://yihangchen-ee.github.io/project_cnc/), CVPR24
[^11]: [Neural Residual Radiance Fields for Streamably Free-Viewpoint Videos](https://aoliao12138.github.io/ReRF/), CVPR23
[^12]: [Drivable Volumetric Avatars using Texel-Aligned Features](https://arxiv.org/pdf/2207.09774), SIGGRAPH 2022
[^13]: [Driving-Signal Aware Full-Body Avatars](https://arxiv.org/pdf/2105.10441), ACM ToG 2021