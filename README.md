# Optimization of Telecommunication Networks (Linear Regression Analysis)

This project focuses on the analysis and optimization of telecommunication networks using **Machine Learning** techniques, specifically **Linear Regression**. By analyzing a real-world or simulated fiber optic dataset, the goal is to identify key factors affecting network performance and develop a robust predictive model for crucial network parameters (e.g., signal attenuation or efficiency).

## 💡 Project Goal

The primary objective is to build a mathematical model that can accurately predict a dependent variable (like signal quality or loss) based on several independent variables within the network data, thereby enabling data-driven decisions for network optimization and predictive maintenance.

## 🌟 Key Features

* **Comprehensive Data Pipeline:** Structured scripts for data loading, preprocessing, and exploratory analysis.
* **Feature Engineering & Analysis:** Detailed analysis of features to understand their correlation and impact on network performance.
* **Predictive Modeling:** Implementation of a Linear Regression model to establish relationships and make predictions.
* **Visualization:** Tools for plotting data distributions, feature relationships, and visualizing model performance metrics.
* **Model Persistence:** Ability to save the trained model for later use in a production or deployment environment.

## 📁 Project Structure & Files

The repository is organized into distinct Python modules for clarity and maintainability:

| File Name | Purpose |
| :--- | :--- |
| `fiber_optic_dataset.csv` | The raw dataset containing network parameters and performance metrics. |
| `DataSet.py` | Handles the initial loading and structuring of the dataset. |
| `DataOverview.py` | Provides summary statistics and an initial overview of the dataset. |
| `DataPreprocessing.py` | Contains functions for cleaning, normalization, and preparing data for modeling. |
| `FeatureAnalysis.py` | Performs exploratory data analysis (EDA) and identifies important features. |
| `LinearRegression.py` | Defines, trains, and evaluates the core Linear Regression model. |
| `Plotting.py` | Module for generating charts and visualizations (e.g., scatter plots, histograms). |
| `SaveModel.py` | Contains the logic for serializing and saving the final trained model object. |
| `app.py` | The main file for executing the entire pipeline or serving as a demonstration interface. |

## 🚀 Getting Started

### 1. Prerequisites

You need Python installed. Install the required data science and machine learning libraries:

```bash
pip install pandas numpy scikit-learn matplotlib
```

### 2.Execution
To run the complete data pipeline (preprocessing, training, analysis, and saving the model), execute the main application file:

```bash
python app.py
```

### 3.Individual Scripts
You can run individual scripts to perform specific tasks:

* To analyze features: python FeatureAnalysis.py

* To train the model: python LinearRegression.py
