# Skinned Gaussian Avatars

> Simple Animated Gaussian Avatars from Multiview SMPL fits.

## Requirements

1. [`moai-mdk==0.1.5a34`](https://github.com/moverseai/moai)
2. [`nvdiffrast==0.3.3`](https://github.com/NVlabs/nvdiffrast)
3. [`rerun-sdk==0.19.0`](https://github.com/rerun-io/rerun)
4. [`plyfile==1.1`](https://github.com/dranjan/python-plyfile)
5. [`pytorch3d==0.7.8+pt2.5.1cu118`](https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md)
6. alpha supporting [`Gaussian splatting`](https://github.com/ashawkey/diff-gaussian-rasterization) which requires a renaming of the package with the following changes applied to `setup.py`:
    ```diff    
    --- setup.py
    - name="diff_gaussian_rasterization",
    - packages=['diff_gaussian_rasterization'],
    + name="diff_gaussian_rasterization_ashawkey",
    + packages=["diff_gaussian_rasterization_ashawkey"],
    ext_modules=[
        CUDAExtension(
    -        name="diff_gaussian_rasterization._C",
    +        name="diff_gaussian_rasterization_ashawkey._C",
    ```
7. [`e3nn==0.5.5`](https://github.com/e3nn/e3nn)
    ```py
    '''e3nn requires a modification of the `wigner_D` function
        in the `e3nn/o3/_wigner.py` file at the L98'''
    # copy to device
    X = so3_generators(l).to(alpha.device)
    ```

## Usage

The fit is a two step process, first acquiring a coarse deformation to better initialize the body's geometry with the actor, and second, fitting the animated Gaussian splatting parameters.

> [!IMPORTANT]
> Two environmental variables need to be set:
>    - `SMPL_ROOT`: the path to the [SMPL](https://smpl.is.tue.mpg.de/) body model data
>    - `SMPL_GENDER`: the actor's gender that was used to reconstruct their motion (see the [`Data`](#Data) subsection)

> [!NOTE]  
> The following commands are run from the root of this repo.

### 1. Coarse Geometry
```sh
python -m moai run fit conf/projects/fit_mesh/main.yaml --config-dir conf DATA_ROOT=PATH/TO/DATA/FOLDER
```
When this step finishes, the output will reside in `/actions/fit/DATE/TIME-fit_gaussian_avatar`. The `offsets.npz` file is needed for the next step.


### 2. Gaussian Splats
```sh
python -m moai run fit conf/projects/skinned_gaussian_avatar/main.yaml --config-dir conf DATA_ROOT=PATH/TO/DATA/FOLDER OFFSETS=STEP1/PATH/TO/OFFSETS METHOD=THE_FIT_TYPE
```
where `THE_FIT_TYPE` is one of `[lbs|lbs_v|qlbs_v|qlbs_sh1_v|qlbs_sh2_v|qlbs_sh3_v]` corresponding to:
- the skinning type (`lbs` or `qlbs`), 
- the vertex derived scaling `_v` or not, 
- and the SH coefficients to use `sh1|sh2|sh3`


> [!WARNING]  
> When using the raw scaling option (without the `_v` suffix) the Gaussian scales are initialized with an absolute metric scale instead of a relative with respect to the vertex areas. Therefore, it is recommended to set a proper value with `model.monads.gaussian_splat_parameters.scale=1e-3` at the command line call. Otherwise, an out-of-memory error will most likely be emmited as each Gaussian rasterizes to a very large amount of screenspace points.


When this step finishes, the output will similarly reside in `actions/fit/DATE/time-skinned_gaussian_avatar` with the `splat.ply` and `splat_for_unity.ply` containing the T-posed avatar's gaussian parameters, and `joints.ply` and `skinned_mesh.ply` containing the skinning related parameters.

### Data

The necessary data to reconstruct an animated Gaussian avatar are:

- `N` multiview frame-aligned videos: `[0,...,N]_color.mp4`, 
- `N` multiview frame-aligned mask videos: `[0,...,N]_mask.mp4`,
- 1 animation parameters file: `data.npz`

An example tree structure follows:
```sh
PATH/TO/DATA
|-  0_color.mp4
|-  0_mask.mp4
|-  1_color.mp4
|-  1_mask.mp4
|-  2_color.mp4
|-  2_mask.mp4
|-  3_color.mp4
|-  3_mask.mp4
|-  4_color.mp4
|-  4_mask.mp4
|-  5_color.mp4
|-  5_mask.mp4
|-  6_color.mp4
|-  6_mask.mp4
|-  7_color.mp4
|-  7_mask.mp4
|-  data.npz
```

The `data.npz` file contains a set of `np.arrays` with the following structure:

```py
>>> import numpy as np
>>> d = np.load(r"PATH/TO/DATA.NPZ")
>>> d.files
['extrinsics', 'intrinsics', 'betas', 'pose', 'transl', 'global_orient', 'time']
>>> for f in d.files: print(f, d[f].shape, d[f].dtype)
...
extrinsics (8, 4, 4) float32
intrinsics (8, 3, 3) float32
betas (10,) float32
pose (1222, 23, 3) float32
transl (1222, 3) float32
global_orient (1222, 3) float32
time (1222,) float64
```

which corresponds to `N` camera extrinsics and intrinsics matrices, `10` shape coefficients, and `T` frames of animation parameters and timestamps in seconds. The animation parameters are the global rotation and translation and the articulation in axis angle format.

> [!TIP]
> It is possible to run with only a subset of the views using the `SUBSET=[X,Y,Z,W]` command line argument, where the list includes the indices of the views to be used.