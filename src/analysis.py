import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    print("🔍 Running Anomaly Detection...")
    
    # Select features for anomaly detection
    features = ['Temperature_C', 'Humidity_pct']
    X = df[features].dropna()
    
    # Initialize Isolation Forest
    # contamination = 0.01 means we expect roughly 1% of the data to be anomalies
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    
    # Fit and predict (-1 is anomaly, 1 is normal)
    df['Anomaly'] = 1  # Default to normal
    
    # Only predict on non-null rows
    valid_idx = X.index
    predictions = model.fit_predict(X)
    
    df.loc[valid_idx, 'Anomaly'] = predictions
    
    anomalies_count = len(df[df['Anomaly'] == -1])
    print(f"⚠️ Found {anomalies_count} anomalous weather days.")
    
    return df

def generate_summary(df, output_path='outputs/reports/summary.txt'):
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write("=== Climate Trend Summary ===\n")
        f.write(f"Total Days Analyzed: {len(df)}\n")
        f.write(f"Max Temperature Recorded: {df['Temperature_C'].max()}°C\n")
        f.write(f"Min Temperature Recorded: {df['Temperature_C'].min()}°C\n")
        f.write(f"Average Yearly Temperature: {df['Temperature_C'].mean():.2f}°C\n")
        f.write(f"Total Anomalies Detected: {len(df[df['Anomaly'] == -1])}\n")
    print(f"✅ Summary saved to {output_path}")