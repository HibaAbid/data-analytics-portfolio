# MSc Information Science Projects

This repository contains selected projects from my **MSc in Information Science**, demonstrating skills in **data analysis, prediction, and visualization**.  
The projects highlight real-world applications using Python, Tableau, machine learning, and statistical modeling techniques.  

---

## 📘 Projects Included

### 1️⃣ Data Science Practicum — Stock Price Analysis and Prediction

**Objective:**  
- Analyze historical stock data to understand trends, volatility, and relative performance across leading companies  
- Apply predictive modeling to forecast future stock prices  
- Visualize insights to support investment and portfolio decisions  

**Research Context:**  
- **Performance Analysis:** Statistical and ML models are used to analyze returns, trends, and volatility  
- **Economic Impact:** Examining the effect of macroeconomic factors such as inflation, interest rates, and political events  

**Dataset Overview:**  
The project focuses on the world’s top companies, including **Apple, Microsoft, Google, Amazon, and Tesla**, and analyzes historical stock prices to extract daily and monthly returns, compare performance relative to market indices, and identify trends and patterns.  

**Key Analytical Insights:**  
- Daily returns vary between different stocks, with top companies showing differing levels of volatility  
- Combined stock and index datasets allow for **relative performance analysis**  
- Visualizations (line charts, bar plots, and scatter plots) reveal trends, sector behavior, and anomalies  
- Verified hypotheses on stock behavior, including variability and correlation with market trends  

**Predictive Modeling & Forecasting:**  
The final part of the project uses a Python script to forecast stock prices based on user-input year and month. The process includes:  
1. **Data Loading:** Load historical stock data from CSV files, including dates, stock symbols, and adjusted close prices (`adj_close`)  
2. **Data Preparation:** Convert date columns to a workable format and structure the data for forecasting  
3. **Model Training:** Train a **Prophet forecasting model** for each selected stock  
4. **Future Forecasts:** Generate predictions for future prices  
5. **Multiple Stocks Forecasts:** Repeat the process for multiple top stocks (AAPL, MSFT, GOOGL, AMZN, TSLA) and calculate the predicted average price per stock  
6. **Results Visualization:** Display forecasts in tables and bar charts for intuitive interpretation  

**Outcome:**  
The project integrates **analytical insights** (returns, volatility, trends) with **predictive forecasts**, providing a comprehensive view of stock behavior. Users can both explore historical performance and generate future price predictions for leading companies.  

**Tools & Techniques:**  
- Python (pandas, matplotlib, seaborn, Prophet)  
- Data visualization and analysis  
- Statistical modeling and predictive analytics  

**Data Access:**  
The dataset is available [here](https://drive.google.com/drive/folders/1w9qGOtTrbuugDNxW06oBdSOkCg5v1HUx)  

---

### 2️⃣ Data Visualization and Analysis — Heart Disease Prediction

**Dataset Overview:**  
- **Source:** Kaggle — [UCI Heart Disease Data](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)  
- **Description:** Clinical data on patients to predict the presence of heart disease, including features like age, sex, chest pain type, blood pressure, cholesterol, and more.  

**Problem Statement:**  
Heart disease is one of the leading causes of mortality worldwide. Early prediction can save lives through preventive care.  
The goal is to **predict the risk of heart disease** based on clinical features.  

**Research Question:**  
Which clinical features (e.g., age, blood pressure, cholesterol, chest pain type) are the strongest predictors of heart disease risk?  

**Hypotheses:**  
- Features such as age, cholesterol levels, chest pain, and blood pressure will significantly influence heart disease risk  
- These features are expected to have higher predictive power compared to other variables  

**Exploratory Data Analysis (EDA):**  
- Understand feature distributions and relationships  
- Identify patterns and anomalies in the dataset  
- Compare model performance using metrics such as ROC AUC  

**Analysis & Visualization:**  
- Applied statistical models and machine learning algorithms for prediction  
- Created visualizations (bar charts, scatter plots, boxplots) to illustrate feature distributions and correlations  
- Evaluated model performance and feature importance  

**Tools & Techniques:**  
- Python (pandas, scikit-learn, matplotlib, seaborn)  
- Tableau (optional, for visualization)  
- Machine learning models for prediction  

---

## 🛠 Tools & Technologies

- Python (3.x): pandas, NumPy, matplotlib, seaborn, scikit-learn, Prophet  
- Tableau for dashboards and visualizations  
- Statistical modeling and predictive analytics  
- Open datasets from Kaggle and financial data sources  

---

## ✅ Outcomes

These projects demonstrate my ability to:  
- Analyze and visualize complex datasets  
- Build predictive models for real-world scenarios  
- Interpret data-driven insights and communicate them effectively  
- Apply technical skills to solve practical problems in finance and healthcare  

---

## 📄 Notes

These projects were completed as part of my **MSc in Information Science**.  
They reflect technical proficiency, analytical thinking, and the ability to translate data into actionable insights.
