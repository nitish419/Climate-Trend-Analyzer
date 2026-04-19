import pandas as pd
import os

def clean_data(input_path='data/raw/climate_data.csv', output_path='data/processed/cleaned_climate_data.csv'):
    df = pd.read_csv(input_path)
    
    # Parse dates
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort chronologically
    df = df.sort_values('Date')
    
    # Handle missing values (forward fill as weather is continuous)
    df.ffill(inplace=True)
    
    # Feature Engineering
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Season'] = df['Month'].apply(lambda x: 'Winter' if x in [12,1,2] else ('Summer' if x in [3,4,5] else ('Monsoon' if x in [6,7,8,9] else 'Post-Monsoon')))
    
    # Calculate 30-day rolling average for temperature smoothing
    df['Temp_30d_Avg'] = df['Temperature_C'].rolling(window=30).mean()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Data cleaned and saved to {output_path}")
    return df

if __name__ == "__main__":
    clean_data()