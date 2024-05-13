from SPConvNets.trainer_modelnet import Trainer
from SPConvNets.options import opt
import os
import pickle

#Run this for training so that accuracies can be saved too

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
    
