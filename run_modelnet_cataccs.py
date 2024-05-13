from SPConvNets.trainer_modelnet import Trainer
from SPConvNets.options import opt
import os
import pickle

"""
This script is used to train the classification model from EPN (Equivariant Point Network) on the ModelNet dataset and save the accuracy scores for each category in a pickle file.

To run the script, use the following command:
CUDA_VISIBLE_DEVICES=0 python run_modelnet_cataccs.py experiment -d PATH_TO_DATASET

- Set the CUDA_VISIBLE_DEVICES environment variable to specify the GPU device to use (e.g., 0 for the first GPU).
- Replace PATH_TO_DATASET with the path to the ModelNet dataset.

The script requires the SPConvNets package, which includes the Trainer class and the options module.

In the script, the model configuration is set using the opt.model.flag and opt.model.model options.
- opt.model.flag is set to 'attention' to use the attention-based model.
- opt.model.model is set to 'cls_so3net_pn' to specify the classification model architecture.

If the script is run in training mode (opt.mode == 'train'), the training parameters can be overridden, such as the batch size (opt.batch_size), learning rate decay rate (opt.train_lr.decay_rate), decay step (opt.train_lr.decay_step), and attention loss type (opt.train_loss.attention_loss_type).

The script iterates over each category in the ModelNet dataset (specified by opt.dataset_path) and performs the following steps:
1. Sets the current category (opt.cat) to the category being processed.
2. Instantiates the Trainer class from SPConvNets with the provided options (opt).
3. Calls the eval() method of the trainer to evaluate the model on the current category and obtain the accuracy score.
4. Stores the accuracy score for the current category in the cataccs dictionary, where the key is the category name and the value is the accuracy score.

After processing all categories, the cataccs dictionary is saved to a pickle file named 'cataccs.pkl' using the pickle module.

The saved pickle file can be later used to analyze the accuracy scores for each category.

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
    cataccs = {}
    for category in os.listdir(opt.dataset_path):
        opt.cat = category
        trainer = Trainer(opt)
        
        cataccs[category] = trainer.eval() 
    with open('cataccs.pkl', 'wb') as f:
        pickle.dump(cataccs, f)
    
