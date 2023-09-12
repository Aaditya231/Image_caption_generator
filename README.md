# Image Caption Generator

![Demo](demo.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

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
