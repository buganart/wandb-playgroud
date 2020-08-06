import wandb
run = wandb.init(entity='bugan', project='sandbox')

artifact = wandb.Artifact(
    'faces', 
    type='dataset', 
    description="A collection of images of faces.", 
    metadata={"resolution": 256},
)

# Recursively add a directory
artifact.add_dir("./test-dataset", name='faces')

run.log_artifact(artifact)

#artifact = run.use_artifact('bugan/tree-gan/dataset-tree:full', type='dataset')
#artifact_dir = artifact.download()


