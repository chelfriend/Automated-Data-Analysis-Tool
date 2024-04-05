# src/report_generation.py

import pandas as pd

def generate_report(summary_stats):
    # Generate report
    report = summary_stats.to_html()

    # Save report to file
    with open('report.html', 'w') as file:
        file.write(report)
