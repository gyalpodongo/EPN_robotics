from SPConvNets.trainer_modelnet import Trainer
from SPConvNets.options import opt
import os

"""
This script is used to train or evaluate the classification model from EPN (Equivariant Point Network) on the ModelNet dataset.

To train the model, use the following command:
CUDA_VISIBLE_DEVICES=0 python run_modelnet.py experiment -d PATH_TO_DATASET

- Set the CUDA_VISIBLE_DEVICES environment variable to specify the GPU device to use (e.g., 0 for the first GPU).
- Replace PATH_TO_DATASET with the path to the ModelNet dataset.

To evaluate a trained model, use the following command:
CUDA_VISIBLE_DEVICES=0 python run_modelnet.py experiment -d PATH_TO_DATASET -r PATH_TO_MODEL --run-mode eval

- Set the CUDA_VISIBLE_DEVICES environment variable to specify the GPU device to use (e.g., 0 for the first GPU).
- Replace PATH_TO_DATASET with the path to the ModelNet dataset.
- Replace PATH_TO_MODEL with the path to the trained model checkpoint.
- Use the --run-mode eval flag to specify the evaluation mode.

The script requires the SPConvNets package, which includes the Trainer class and the options module.

In the script, the model configuration is set using the opt.model.flag and opt.model.model options.
- opt.model.flag is set to 'attention' to use the attention-based model.
- opt.model.model is set to 'cls_so3net_pn' to specify the classification model architecture.

If the script is run in training mode (opt.mode == 'train'), the training parameters can be overridden, such as the batch size (opt.batch_size), learning rate decay rate (opt.train_lr.decay_rate), decay step (opt.train_lr.decay_step), and attention loss type (opt.train_loss.attention_loss_type).

The Trainer class from SPConvNets is instantiated with the provided options (opt), and the train() or eval() method is called based on the specified mode (opt.mode).

Note: Make sure to have the required dependencies installed and the SPConvNets package available in your Python environment before running this script.
"""


if __name__ == '__main__':
    opt.model.flag = 'attention'
    opt.model.model = "cls_so3net_pn"

    if opt.mode == 'train':
        # overriding training parameters here
        opt.batch_size = 6
        opt.train_lr.decay_rate = 0.5
        opt.train_lr.decay_step = 20000
        opt.train_loss.attention_loss_type = 'default'

    trainer = Trainer(opt)
    if opt.mode == 'train':
        trainer.train()
    elif opt.mode == 'eval':
        trainer.eval() 
