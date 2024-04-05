# src/main.py

import pandas as pd
from data_cleaning import clean_data
from exploratory_data_analysis import perform_eda
from report_generation import generate_report

def main():
    # Load data
    data = pd.read_csv('../data/sample_data.csv')

    # Clean data
    clean_data(data)

    # Perform EDA
    summary_stats = perform_eda(data)

    # Generate report
    generate_report(summary_stats)

if __name__ == "__main__":
    main()
