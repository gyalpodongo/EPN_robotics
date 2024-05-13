
# Equivariant Point Network (EPN) for Robotics

This repository contains a revamped version of the code (in PyTorch) for [Equivariant Point Network for 3D Point Cloud Analysis](https://arxiv.org/abs/2103.14147)  (CVPR'2021) by Haiwei Chen, [Shichen Liu](https://shichenliu.github.io/), [Weikai Chen](http://chenweikai.github.io/) and [Hao Li](http://www.hao-li.com/Hao_Li/Hao_Li_-_about_me.html). The code here has been adapted for modern dependencies, reduced to just the classification model and tested with the YCB robotics dataset.

Another big inspiration for this project comes from [3DSGrasp]("https://github.com/NunoDuarte/3DSGrasp") due to how attention can be key in robostic grasping methods. We thank the authors of both papers for their massive help with this project. 

## Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Experiments](#experiments)
4. [Contact](#contact)

## Introduction

EPN is a SE(3)-equivariant network model that is designed for deep point cloud analysis. The core of the architecture is the **SE(3) Separable Convolution** that combines two sequential, equivariant convolution layers to approximate convolution in the SE(3) space. With the incorporation of an attention mechanism, the EPN network model can be used to extract both SE(3) equivariant features and selectively pooled invariant features for various feature learning tasks.

![](https://github.com/nintendops/EPN_PointCloud/blob/main/media/spconv.png)

Thanks to these properties, the classification process becomes more accurate with a lot less data needed. Thus, we believe that this can be also key in a robotics grasping setting. We test this model against YCB after being inspired by developments such as [3DSGrasp]("https://github.com/NunoDuarte/3DSGrasp") and see whether our classification model could outperform theirs.

## Installation

The code has been tested on Python3.10.2, PyTorch 2.0.1 and CUDA (12). To install all requirements, datasets, models and set up the repo just run:
```
source setup.sh
```

This process may take a while due to all the steps it follows as downloading datasets, formatting them and installing the Vision-Graphics deep learning ToolKit developed for EPN.

## Experiments

**Datasets**

The rotated Modelnet40 point cloud dataset is generated from the [Aligned Modelnet40 subset](https://github.com/lmb-freiburg/orion) and can be downloaded using this [link](https://drive.google.com/file/d/1xRoYjz2KCwkyIPf21E-WKIZkjLYabPgJ/view?usp=sharing). Through our training we were able to outpreform the original EPN model in the classification task with an accuracy score of **88.39%**. 

![](https://github.com/gyalpodongo/EPN_robotics/blob/main/accuracy_plotModenet40.png)

The rotated YCB40 point cloud dataset is generated from the [YCB dataset]() and can be downloaded using this [link]()

**Pretrained Model**

Pretrained model for EPN ModelNet40 can be downloaded using this [link](https://drive.google.com/file/d/1vy9FRGWQsuVi4nf--YIqg_8yHFiWWJhh/view?usp=sharing)
Pretrained model for EPN YCB40 can be downloaded using this [link](https://drive.google.com/file/d/1vy9FRGWQsuVi4nf--YIqg_8yHFiWWJhh/view?usp=sharing)


**Training**

The following lines can be used for the training of each experiment using either EvenAlignedModelNet40PC or YCB40 as the path to dataset.

```
# modelnet classification
CUDA_VISIBLE_DEVICES=0 python run_modelnet.py experiment -d PATH_TO_DATASET
```

**Evaluation**

The following lines can be used for the evaluation of each experiment using either EvenAlignedModelNet40PC or YCB40 as the path to dataset. Make sure to use the correct weights when evaluating the model's performance. Furthermore, this will ensure that the accuracy for each category will be recorded in a file called `cataccs.pkl`.


```
# modelnet classification
CUDA_VISIBLE_DEVICES=0 python run_modelnet_cataccs.py experiment -d PATH_TO_DATASET -r PATH_TO_MODEL --run-mode eval
```



**Visualization**



## Contact

Haiwei Chen: chw9308@hotmail.com
Any discussions or concerns are welcomed!

**Citation**
If you find our project useful in your research, please consider citing:

```
@article{chen2021equivariant,
  title={Equivariant Point Network for 3D Point Cloud Analysis},
  author={Chen, Haiwei and Liu, Shichen and Chen, Weikai and Li, Hao and Hill, Randall},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={14514--14523},
  year={2021}
}
```
