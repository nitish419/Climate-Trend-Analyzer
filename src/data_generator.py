import pandas as pd
import numpy as np
import os

def generate_synthetic_data(output_path='data/raw/climate_data.csv'):
    np.random.seed(42)
    dates = pd.date_range(start='2000-01-01', end='2023-12-31', freq='D')
    n_days = len(dates)
    
    # Base temperature with seasonal sine wave (Peak in May, Low in Dec)
    # Modeling roughly around a tropical region
    time_rad = np.linspace(0, 24 * np.pi, n_days) # 24 years
    base_temp = 25 + 8 * np.sin(time_rad - np.pi/2) 
    
    # Add long-term global warming trend (approx +1.5 degrees over 24 years)
    warming_trend = np.linspace(0, 1.5, n_days)
    
    # Add random daily noise
    noise = np.random.normal(0, 2, n_days)
    
    temperatures = base_temp + warming_trend + noise
    
    # Simulate rainfall (mostly 0, with spikes during 'monsoon' months)
    rainfall = np.where(dates.month.isin([6, 7, 8, 9]), np.random.exponential(scale=10, size=n_days), np.random.exponential(scale=1, size=n_days))
    
    # Create anomalies (Extreme heatwaves or sudden downpours)
    anomaly_indices = np.random.choice(n_days, size=50, replace=False)
    temperatures[anomaly_indices] += np.random.choice([8, -8], size=50) # Sudden spikes or drops
    
    df = pd.DataFrame({
        'Date': dates,
        'Temperature_C': np.round(temperatures, 2),
        'Rainfall_mm': np.round(rainfall, 2),
        'Humidity_pct': np.clip(np.round(np.random.normal(60, 15, n_days)), 10, 100)
    })
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Synthetic dataset generated at {output_path}")

if __name__ == "__main__":
    generate_synthetic_data()