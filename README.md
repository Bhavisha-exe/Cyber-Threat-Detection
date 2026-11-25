# Cyber Threat Detection Using Machine Learning

## Project Overview

Cyber Threat Detection is a machine learning-based project developed to identify potential cyber threats by analyzing network traffic data. The project uses the NSL-KDD dataset, which contains network traffic records used for detecting normal and malicious activities. A Decision Tree classification algorithm is trained using Python in Google Colab to classify network traffic and identify possible attacks. The trained model and its required encoders are saved as `.pkl` files using Joblib. A web application is developed using Flask, HTML, and CSS, allowing users to enter network traffic details and receive a prediction through a simple and user-friendly interface.

## Technologies Used

- Python – Programming language
- Machine Learning – Decision Tree Classification
- Pandas and NumPy – Data handling and processing
- Scikit-learn – Model training and data encoding
- Joblib – Saving and loading the trained model and encoders
- Flask – Backend web application framework
- HTML and CSS – Frontend interface
- Google Colab – Model development and training
- Visual Studio Code – Application development

## Dataset

The project uses the NSL-KDD dataset, consisting of:
- `KDDTrain+.txt` – Training dataset
- `KDDTest+.txt` – Testing dataset

## Project Features

- Machine learning-based network traffic classification.
- Detection of normal and potentially malicious network activities.
- Trained Decision Tree model.
- Flask-based web interface.
- Prediction results displayed through a simple interface.

## Project Structure

- `dataset/` – Contains the training and testing datasets.
- `model/` – Contains the trained model and encoder files.
- `templates/` – Contains the HTML web page.
- `app.py` – Main Flask application.
- `model_test.py` – Model testing script.
- `Untitled13.ipynb` – Google Colab notebook containing the model development and training work.
- `requirements.txt` – Python dependencies required to run the project.

## Objective

The main objective of this project is to demonstrate how machine learning can be used in cybersecurity to analyze network traffic and identify potential threats. It also demonstrates the integration of a trained machine learning model with a Flask-based web application.

