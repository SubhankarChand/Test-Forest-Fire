# Test Forest Fire

This project focuses on predicting forest fire occurrences using machine learning models. It utilizes Ridge Regression and data preprocessing techniques to provide accurate predictions based on input features like temperature, relative humidity, wind speed, and more.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The **Test Forest Fire** project aims to predict forest fire behavior using a Ridge Regression model. The model takes input data such as temperature, relative humidity, wind speed, and other environmental factors to predict the fire weather index (FWI).

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- Numpy
- HTML/CSS (for the frontend)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/SubhankarChand/Test-Forest-Fire.git
   cd Test-Forest-Fire

## Install the required dependencies:
```bash
pip install -r requirements.txt
Place the ridge.pkl and scaler.pkl models in the models/ directory.
```

## Run the Flask application:
```bash
python application.py
```

## Usage
- Navigate to the prediction form at the root URL.
- Input the required environmental parameters (Temperature, RH, Wind Speed, etc.).
- Submit the form to get the predicted FWI value.

## File Descriptions
application.py: Main Flask application handling routes and prediction logic.
models/: Directory containing the pre-trained ridge.pkl and scaler.pkl models.
templates/: Contains HTML files (home.html) for the web interface.
static/: Directory for static files (if any).
requirements.txt: List of dependencies for the project.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.
