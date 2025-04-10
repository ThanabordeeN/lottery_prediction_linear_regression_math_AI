# AI for Electronics Engineering - Linear Regression Lottery Prediction

This repository contains materials for the AI Mathematics class in the Electronics Engineering program at Suranaree University of Technology (SUT). The project demonstrates how to build a Linear Regression model using TensorFlow to predict lottery numbers.

## Repository Contents

This repository includes:

1. `main.ipynb` - Basic Linear Regression model for lottery number prediction
2. `main_one_hot.ipynb` - Enhanced model using One-Hot Encoding for categorical variables

## Prerequisites

To run these notebooks, you'll need:

- Python 3.6+
- TensorFlow 2.x
- pandas
- matplotlib
- scikit-learn
- numpy

You can install the required packages using:
```
pip install tensorflow pandas matplotlib scikit-learn numpy
```

## Dataset

The project uses a Thai lottery dataset. You need to download it from [this link](https://drive.google.com/file/d/1qpXVeS2oEf-DW_jFTusoNwkUJIM2x3ME/view) and place the `lottery.csv` file in the same directory as the notebooks.

## How to Use

1. Download the dataset from the link above
2. Open either notebook in Jupyter or Google Colab
3. Run the cells sequentially to:
   - Load and preprocess the data
   - Create and train the model
   - Evaluate performance
   - Make predictions

## Model Differences

The two notebooks demonstrate different approaches:

- `main.ipynb`: Uses basic numerical features (Date, Month, Year)
- `main_one_hot.ipynb`: Enhances the model with categorical features using one-hot encoding for weekday names

## Learning Outcomes

Students will learn:
- Data preprocessing techniques
- Feature engineering with one-hot encoding
- Building neural networks with TensorFlow
- Model evaluation and visualization
- Saving and reusing trained models

## Note

This project is intended for educational purposes. Lottery prediction is used as an engaging example to teach machine learning concepts, but real lottery numbers are random and unpredictable.

## License

This project is provided for educational use at Suranaree University of Technology.
