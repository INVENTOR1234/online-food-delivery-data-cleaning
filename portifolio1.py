import os
import pandas as pd

# Automatically locate the folder where this script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, 'online food delivery dataset.csv')

print(f"Reading file from: {input_file}")

# 1. Load the dataset
try:
    df = pd.read_csv(input_file)
    print("File loaded successfully!\n")
    print("Initial Shape:", df.shape)
    
    # 2. Clean column headers (lowercase, replace spaces with underscores)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # 3. Handle missing values (e.g., fill missing age entries with median)
    if 'age' in df.columns:
        df['age'] = df['age'].fillna(df['age'].median())

    # 4. Clean text columns (strip whitespace, convert to Title Case)
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip().str.title()

    # 5. Remove duplicates
    df = df.drop_duplicates()

    # 6. Save the cleaned CSV file into the same FREELANCING folder
    output_file = os.path.join(script_dir, 'cleaned_online_food_delivery.csv')
    df.to_csv(output_file, index=False)
    
    print("\nCleaned dataset shape:", df.shape)
    print(f"Cleaned file successfully saved to: {output_file}")

except FileNotFoundError:
    print("\n[ERROR] Could not find the CSV file.")
    print("Make sure 'online food delivery dataset.csv' is named correctly in your FREELANCING folder.")