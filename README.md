# Online Food Delivery Data Cleaning & Preprocessing

## 📌 Project Overview
This project focuses on cleaning and standardizing raw customer survey data from an online food delivery platform. The pipeline cleans messy demographic records, standardizes column headers, handles missing entries, and exports a structured dataset for analysis.

## 🛠️ Tools & Technologies
* **Python 3.x**
* **Pandas** for data manipulation
* **OS Module** for path resolution across environments

## 🧼 Key Cleaning Steps Completed
1. **Header Normalization:** Converted all column names to lowercase `snake_case` format (`marital_status`, `monthly_income`).
2. **Missing Value Imputation:** Handled null age fields using median values.
3. **Categorical Formatting:** Cleaned up whitespace and converted string fields to Title Case.
4. **Deduplication:** Identified and purged duplicate records.
5. **Data Export:** Processed and saved output as `cleaned_online_food_delivery.csv`.

## 📁 Files Included
* `portfolio1.py` - Python cleaning script
* `online food delivery dataset.csv` - Raw dataset
* `cleaned_online_food_delivery.csv` - Final cleaned dataset
