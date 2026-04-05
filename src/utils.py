import pandas as pd
def generate_summary_report(session_start,csv_path="emissions.csv"):
    df = pd.read_csv(csv_path)
    
    # 1. Convert CSV timestamp strings to Python datetime objects
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # 2. FILTER: Only keep rows created AFTER this script started
    session_df = df[df['timestamp'] >= session_start].copy()

    if session_df.empty:
        print("XXX No new data found for this session.")
        return None

    # 3. Aggregate only the session data
    summary = session_df.groupby('project_name').agg({
        'duration': 'mean',
        'emissions': 'mean',
        'energy_consumed': 'mean'
    }).reset_index()
    
    # Add a custom metric: Efficiency Score (Lower is Better)
    summary['efficiency_score'] = summary['energy_consumed'] * summary['duration']
    summary = summary.sort_values(by='energy_consumed')
    
    print("\n-- FINAL GREEN-OPS REPORT --")
    print(summary.to_string(index=False))
    
    summary.to_csv("reports/summary_report.csv", index=False)
    return summary