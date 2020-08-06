import json

import numpy as np
import trimesh
import wandb

with open("sample_tree_80_54d6ee68.pts.json") as f:
    voxel_list = json.load(f)

voxels = np.zeros([64, 64, 64], dtype=bool)

for x, y, z in voxel_list:
    voxels[x, y, z] = True

voxelmesh = trimesh.voxel.VoxelGrid(trimesh.voxel.encoding.DenseEncoding(voxels)).marching_cubes
voxelmesh.export("voxel_mesh_from_sample_tree.obj")

run = wandb.init(
    entity='bugan',
    project='sandbox', 
    notes="Logging 3d mesh converted from generated voxels via marching_cubes.",
    save_code=True,
    config={"hello": "world"},
)

wandb.log({"a_tree": wandb.Object3D(open("voxel_mesh_from_sample_tree.obj"))})


