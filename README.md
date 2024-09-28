# Spam Detection API

## Overview

This project is a **Spam Detection API** built using a machine learning model. The API is designed to predict whether a given text message is **spam** or **ham** (legitimate). The goal of this project is to provide an easy-to-use, containerized web service that can be integrated into larger applications to identify and filter spam messages.

The API has been developed using `Flask` and `scikit-learn`, and is fully containerized using `Docker` for seamless deployment. This README file will guide you through the installation, usage, and deployment of the API.

## Features

- **Machine Learning Model**: Utilizes a pre-trained spam detection model (`model.pkl` and `vectorizer.pkl`) based on **Naive Bayes** with a high accuracy (98%) and recall (76%).
- **RESTful API**: A simple HTTP POST endpoint (`/detect-spam`) to predict whether a message is spam or not.
- **Docker Support**: Easily deploy the API using Docker, ensuring environment consistency and ease of deployment.
- **Input Validation**: Validates input to ensure a smooth user experience and accurate predictions.

## Project Structure

The repository is organized as follows:

Root/
 data/
 models/
  model.pkl
  vectorizer.pkl
 notebooks/
  Tutorial.ipynb
 src/
   init.py
   app.py
   spam_model.py
 poetry.lock
 pyproject.toml
 README.md
 requirements.txt

## Requirements

- Python 3.12+
- poetry
- Flask
- scikit-learn
- joblib
- Docker (optional, for containerization)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/getrichthroughcode/spam-detector-api.git
cd spam-detector-api
```

### 2. Install dependancies 

This project uses [Poetry](https://python-poetry.org) for dependency management. Make sure you have Poetry installed:

```bash
pip install poetry 
````
Install the project dependencies:
```bash
poetry install
```

