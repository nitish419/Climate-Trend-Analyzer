# 🌍 Climate Trend Analyzer: Time-Series & Anomaly Detection

## 📌 Project Overview
The **Climate Trend Analyzer** is an end-to-end data pipeline built in Python. It simulates, processes, and analyzes two decades of daily climate data to identify long-term global warming trends, seasonal patterns, and extreme weather anomalies using Machine Learning.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Isolation Forest)
* **Visualization:** Matplotlib, Seaborn

## 📊 Key Features
1.  **Automated Data Preprocessing:** Handles missing values and extracts temporal features.
2.  **Trend Analysis:** Uncovers macro-level temperature shifts over a 24-year period.
3.  **Machine Learning Anomaly Detection:** Utilizes an Isolation Forest model to flag extreme weather events without manual thresholding.

## ⚙️ Architecture
Raw Data $\rightarrow$ Preprocessing $\rightarrow$ Feature Engineering $\rightarrow$ ML Anomaly Engine $\rightarrow$ Visualization

## 🚀 How to Run
1. Clone the repository: `git clone https://github.com/yourusername/Climate-Trend-Analyzer.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Execute the pipeline: `python main.py`
4. View generated insights in the `outputs/figures/` folder.

## 💡 Learning Outcomes
* Mastered time-series data manipulation with Pandas.
* Implemented unsupervised learning algorithms for anomaly detection.
* Developed a modular, production-ready project structure.
