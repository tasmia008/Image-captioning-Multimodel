# Image Captioning Project

This repository contains an image captioning project that generates descriptive captions for images using deep learning techniques. The project leverages a combination of convolutional neural networks (CNNs) for image feature extraction and recurrent neural networks (RNNs) for sequence generation.



## Introduction
Image captioning is a challenging task that involves generating a textual description for a given image. This project implements a deep learning model that generates captions by combining the visual understanding of CNNs with the language generation capabilities of RNNs.

## Features
- **Image preprocessing**: Utilizes pre-trained CNNs (like VGG16, ResNet) for feature extraction.
- **Caption generation**: Implements RNNs (LSTM/GRU) to generate sequences of words describing the images.
- **Beam Search**: Implements beam search to improve the quality of generated captions.
- **Training and evaluation scripts**: Includes scripts to train the model and evaluate its performance on a test set.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/tasmia008/Image-captioning-Multimodel.git
    cd Image-captioning-Multimodel
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Dataset
The project uses the Flickr Image dataset for training and evaluation. Download the dataset from [Flickr Image dataset](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset) and place it in the `data/` directory.

## Model Architecture
The model consists of two main parts:
1. **Encoder**: A pre-trained CNN (e.g., VGG16, ResNet) that extracts features from images.
2. **Decoder**: An RNN (e.g., LSTM, GRU) that generates captions based on the extracted features.

## Results
The model achieves competitive results on the Flickr Image dataset. Example captions generated by the model are as follows:
- ![Example 1](data/1000092795.jpg)  <br>
"Two young guys with shaggy hair look at their hands while hanging out in the yard ."
- ![Example 2](data/10002456.jpg)  <br>
"Two young , White males are outside near many bushes. "


## License
Th
