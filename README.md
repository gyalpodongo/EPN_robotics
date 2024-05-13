
# Equivariant Point Network (EPN) for Robotics

This repository contains a revamped version of the code (in PyTorch) for [Equivariant Point Network for 3D Point Cloud Analysis](https://arxiv.org/abs/2103.14147). The code here has been adapted for modern dependencies, reduced to just the classification model and tested with the YCB robotics dataset.

Another big inspiration for this project comes from [3DSGrasp]("https://github.com/NunoDuarte/3DSGrasp") due to how attention can be key in robostic grasping methods. 

We thank the authors of both projects for their guidance with this project. 

## Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Experiments](#experiments)
<!-- 4. [Contact](#contact) -->

## Introduction

EPN is a SE(3)-equivariant network model that is designed for deep point cloud analysis. The core of the architecture is the **SE(3) Separable Convolution** that combines two sequential, equivariant convolution layers to approximate convolution in the SE(3) space. With the incorporation of an attention mechanism, the EPN network model can be used to extract both SE(3) equivariant features and selectively pooled invariant features for various feature learning tasks.

![](https://github.com/nintendops/EPN_PointCloud/blob/main/media/spconv.png)

Thanks to these properties, the classification process becomes more accurate with a lot less data needed. Thus, we believe that this can be also key in a robotics grasping setting. We test this model against YCB after being inspired by developments such as [3DSGrasp]("https://github.com/NunoDuarte/3DSGrasp") and see whether our classification model could outperform theirs.

## Installation

The code has been tested on Python3.10.2, PyTorch 2.0.1 and CUDA (12) in an Nvidia A100. To install all requirements, datasets, models and set up the repo just run:

```
source setup.sh
```

This process will take a while due to all the steps it follows as downloading datasets, formatting them and installing the Vision-Graphics deep learning ToolKit developed for EPN. You won't need to downlaod any of the weights/datasets below if you run `setup.sh` succesfully.

For furture use, you'll have to activate the virtual environment using:

```
source venv/bin/activate
```
## Experiments

**Datasets**


**Rotated Modelnet40**
The rotated Modelnet40 point cloud dataset is generated from the [Aligned Modelnet40 subset](https://github.com/lmb-freiburg/orion) and can be downloaded using this [link](https://drive.google.com/file/d/1xRoYjz2KCwkyIPf21E-WKIZkjLYabPgJ/view?usp=sharing). Through our training we were able to outpreform the original EPN model in the classification task with an accuracy score of **88.39%**. 

![](https://github.com/gyalpodongo/EPN_robotics/blob/main/accuracy_plotModenet40.png)

**Rotated YCB40**

The rotated YCB40 point cloud dataset is generated from the [YCB dataset](https://www.ycbbenchmarks.com/) and can be downloaded using this [link](https://drive.google.com/file/d/1rnJP3Q2zvcj5uImxRu8yYwgk0O7md8dJ/view?usp=drive_link). We obtained very promising results as our EPN was able to classify the objects within YCB with an accuracy score of **89.74%**. 3DSGrasp score was of **76%**, however their classificaiton process involved different steps, such as doing the classfication after their own ML model for completion created a new point cloud. Whilst this results isn't directly comparable we believe if we can implement EPN into their pileine, we could get higher results. Furthermore, we reduce their original dataset from 56 to 40 objects to fit into our EPN model and the pointclouds are reduced from 8092 to 2048 per image due to our GPU capacity.

![](https://github.com/gyalpodongo/EPN_robotics/blob/main/accuracy_plotYCB40.png)


**Extra Datasets**

If you want to use another dataset or expand the current one on YCB40, you can use the `createYCB40.py` script which will trasfrom a folder of `.xyz` files into the required format for our model of `.ply` and `.mat` files. Refer to the folder structure of `3dsgrasp_ycb_train_test_split/` to do this succesfully.

**Pretrained Model**

Pretrained model for EPN ModelNet40 and YCB40 will be under the names of `spconv_modelnet` and `spconv_ycb.pth` respectively.

**Training**

The following lines can be used for the training of each experiment using either EvenAlignedModelNet40PC or YCB40 as the path to dataset.

```
# modelnet classification
CUDA_VISIBLE_DEVICES=0 python run_modelnet.py experiment -d PATH_TO_DATASET
```

This will create a `.pth` file which will be in `trained_models/playground/model_TIME/ckpt`. If you want to edit the options such as when to save a checkpoint path, or evaluate the model or log results, you can do it in the `SPConvNets/options.py` file.

**Evaluation**

The following lines can be used for the evaluation of each experiment using either `EvenAlignedModelNet40PC` or `YCB40` as the path to dataset. If you use the pretrained weights, make sure to use the correct weights when evaluating the model's performance which can be either `spconv_modelnet.pth` or `spconv_ycb.pth` respectively. Otherwise, you can use your own weights. Furthermore, this will script ensure that the accuracy for each category will be recorded in a file called `cataccs.pkl`.


```
# modelnet classification
CUDA_VISIBLE_DEVICES=0 python run_modelnet_cataccs.py experiment -d PATH_TO_DATASET -r PATH_TO_MODEL --run-mode eval
```

**Visualization**

To visualize the results after evaluation, within the `visualize.py`, make sure you use the correct `.pkl` for the categories accuracies. Then you can just run 
```
python visualize.py
```

This will generate a file called `accuracy_plot.png` where you can see how well the model classifies each object by analyzing thei respective equaivariant properties.

Furthermore, if you want to visualize any fo the point clouds you can use our `point_cloud.py` script.

<!-- 
## Contact

Gyalpo Dongo: gyalpodongo@gmail.com
Any discussions or concerns are welcomed! -->


