import wandb
import trimesh

m = trimesh.load(".../mustard_reaching_1_1.obj")
v = m.voxelized(1.0)
remeshed = v.marching_cubes
remeshed.export("remeshed_tree.obj")

run = wandb.init(
    entity="bugan",
    project="sandbox",
    notes="Logging 3d mesh converted from generated voxels.",
    save_code=True,
    config={"hello": "world"},
)

for loss in [1.0, 0.2, 0.1]:
    wandb.log(dict(loss=loss))

wandb.log({"a_tree": wandb.Object3D(open("remeshed_tree.obj"))})
