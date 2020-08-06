import wandb
run = wandb.init(
    entity='bugan',
    project='sandbox', 
    notes="Runnign in dirty git repo with save_code=True",
    save_code=True,
    config={"hello": "world"},
)

for loss in [1.0, 0.2, 0.1]:
    wandb.log(dict(loss=loss))
