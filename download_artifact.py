import wandb
run = wandb.init(entity='bugan', project='tree-gan')

artifact = run.use_artifact('bugan/tree-gan/dataset-tree:full', type='dataset')
artifact_dir = artifact.download()


