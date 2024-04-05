# src/data_cleaning.py

import pandas as pd

def clean_data(data):
    # Handle missing values
    data.dropna(inplace=True)

    # Handle outliers
    # Add your outlier handling code here

    # Handle inconsistencies
    # Add your code to handle inconsistencies

    return data
