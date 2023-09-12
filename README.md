# Image Caption Generator

![alt text](https://github.com/Aaditya231/Image_caption_generator/blob/main/images/Screenshot%202023-09-13%20005013.png)
![alt text](https://github.com/Aaditya231/Image_caption_generator/blob/main/images/Screenshot%202023-09-13%20005110.png)


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


## Introduction

The Image Caption Generator is a Python-based project that generates descriptive captions for images. It uses deep learning techniques to analyze the contents of an image and generate human-readable captions that describe the scene or objects within the image.

This repository provides the source code and instructions for setting up and using the Image Caption Generator.

## Features

- Upload an image and generate descriptive captions.
- Easily integrate the generator into your own projects.
- Clean and user-friendly web interface.
- Utilizes deep learning for accurate image analysis.
- Customizable to suit your specific needs.
- If you have a load of images and you want to sort them according to some keywords, pass the images through the model and sort them without opening all the images.

## Getting Started

### Prerequisites

Before you can use the Image Caption Generator, ensure you have the following prerequisites installed:

- Python 3.x
- Flask (for the web interface)
- TensorFlow (for deep learning)
- Other required dependencies (specified in the project files)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/image-caption-generator.git
   cd image-caption-generator
2. First run the image_caption notebook which will generate feature.pkl and main_model.h5 file
3. Now simply run app.py

## Usage
- Run the Flask web application:
python app.py
- Open your web browser and navigate to http://localhost:5000.

- Click on the "Upload Image" button to select an image for caption generation.

- After uploading, click the "Generate Caption" button to see the generated caption for the image.
