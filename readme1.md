# 📌 Level 3 - Task 1: Predictive Modeling

## 📝 Objective  
This task involves building a **predictive regression model** to forecast the **aggregate rating** of a restaurant based on its features. The main goals are:  

- **Build a regression model** to predict restaurant ratings.  
- **Split the dataset** into training and testing sets.  
- **Evaluate model performance** using appropriate metrics.  
- **Experiment with different algorithms** like Linear Regression, Decision Trees, and Random Forest.  

## 📂 Files  
- **task1.py** → Python script for predictive modeling.  
- **Enhanced_Dataset_Task3.csv** → Processed dataset with extracted features.  

## 📊 Steps Performed  

### 1️⃣ **Data Preparation**  
- Loaded the dataset and performed necessary preprocessing.  
- Selected relevant features for prediction.  
- Split data into **training (80%)** and **testing (20%)** sets.  

### 2️⃣ **Model Building**  
- Built regression models using:  
  - **Linear Regression**  
  - **Decision Trees**  
  - **Random Forest**  
- Trained the models on the dataset.  

### 3️⃣ **Model Evaluation**  
- Evaluated models using:  
  - **Mean Absolute Error (MAE)**  
  - **Mean Squared Error (MSE)**  
  - **R² Score**  
- Compared the performance of different models.  

## 🔍 Key Findings  
- The **Random Forest model** provided the best prediction accuracy.  
- **Feature importance analysis** helped identify the most influential factors.  
- Results show that **price range, votes, and online delivery availability** impact ratings.  

## 🚀 How to Run  
Ensure you have the required libraries installed:  

```bash
pip install pandas numpy sklearn matplotlib seaborn