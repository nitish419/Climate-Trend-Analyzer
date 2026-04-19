from src.data_generator import generate_synthetic_data
from src.preprocessing import clean_data
from src.analysis import detect_anomalies, generate_summary
from src.visualization import plot_trends

def run_pipeline():
    print("🚀 Starting Climate Trend Analyzer Pipeline...")
    
    # Step 1: Generate Data
    generate_synthetic_data()
    
    # Step 2: Clean and Preprocess
    df = clean_data()
    
    # Step 3: Analyze & Detect Anomalies
    df = detect_anomalies(df)
    generate_summary(df)
    
    # Step 4: Visualize
    plot_trends(df)
    
    # Save final dataset with anomaly labels
    df.to_csv('data/processed/final_analyzed_data.csv', index=False)
    
    print("🎉 Pipeline Execution Complete! Check the 'outputs' folder.")

if __name__ == "__main__":
    run_pipeline()