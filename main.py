import torch
from src.models import get_model, get_dummy_input
from src.utils import generate_summary_report
from src.profiler import GreenProfiler,benchmark_model
from src.visualizer import GreenVisualizer
import os
from datetime import datetime
from codecarbon import OfflineEmissionsTracker as EmissionsTracker


def run_audit():
    # 1. Setup
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_list = ["resnet18", "resnet50", "mobilenet_v2","vit_b_16"]
    results_dir = "data/raw"
    os.makedirs(results_dir, exist_ok=True)

    print(f"---  Running on: {device.upper()}")

    
    # 2. Execution Loop
    for model_name in model_list:
        try:
            dummy_input = get_dummy_input(model_name, device)
            # Run the professional benchmark
            # The 'iterations' ensures we have enough data to average out energy spikes
            benchmark_model(model_name, dummy_input, iterations=100)
            
            print(f" {model_name} audit complete.")
        except Exception as e:
            print(f"XXX Failed to profile {model_name}: {e}")

if __name__ == "__main__":
    session_start = datetime.utcnow()
    run_audit()
    if os.path.exists("emissions.csv"):
        summary = generate_summary_report(session_start,"emissions.csv")
        
        #Professional Visualization
        print("Generating visual reports...")
        viz = GreenVisualizer()
        viz.plot_energy_vs_latency(summary)
        viz.plot_carbon_footprint(summary)
        
    print("--- ALL TASKS COMPLETE. Check the 'reports/' folder for results.")