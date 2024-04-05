# src/exploratory_data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(data):
    # Summary statistics
    summary_stats = data.describe()

    # Data visualization
    sns.pairplot(data)
    plt.savefig('pairplot.png')

    # Add more EDA tasks as needed

    return summary_stats
