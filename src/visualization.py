import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set visual style
sns.set_theme(style="darkgrid")

def plot_trends(df, output_dir='outputs/figures/'):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Yearly Temperature Trend
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Year', y='Temperature_C', errorbar=None, color='coral')
    plt.title('Average Yearly Temperature Trend (2000-2023)', fontsize=14)
    plt.ylabel('Temperature (°C)')
    plt.xlabel('Year')
    plt.savefig(os.path.join(output_dir, 'yearly_temp_trend.png'))
    plt.close()
    
    # 2. Seasonality Boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Month', y='Temperature_C', palette='viridis')
    plt.title('Monthly Temperature Distribution', fontsize=14)
    plt.savefig(os.path.join(output_dir, 'monthly_seasonality.png'))
    plt.close()

    # 3. Anomaly Scatter Plot
    plt.figure(figsize=(14, 6))
    sns.scatterplot(data=df, x='Date', y='Temperature_C', hue='Anomaly', 
                    palette={1: 'lightblue', -1: 'red'}, alpha=0.6, s=20)
    plt.title('Detected Climate Anomalies (Extreme Heat/Cold)', fontsize=14)
    plt.savefig(os.path.join(output_dir, 'anomaly_scatter.png'))
    plt.close()
    
    print(f"✅ Visualizations saved to {output_dir}")