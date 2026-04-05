import time
import torch
from codecarbon import OfflineEmissionsTracker as EmissionsTracker
from src.models import get_model, get_dummy_input

class GreenProfiler:
    """
    A Professional Context Manager for AI Energy Benchmarking.
    """
    def __init__(self, run_name, device="cpu"):
        self.run_name = run_name
        self.device = device
        # Initialize CodeCarbon in 'offline' mode to avoid network
        self.tracker = EmissionsTracker(project_name=self.run_name,measure_power_secs=0.5, save_to_file=True, log_level='error')

    def __enter__(self):
        print(f" [START] Profiling: {self.run_name} on {self.device}")
        self.start_time = time.perf_counter()
        self.tracker.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        emissions = self.tracker.stop()
        self.end_time = time.perf_counter()
        
        duration = self.end_time - self.start_time
        print(f" [FINISH] {self.run_name} | Duration: {duration:.2f}s | CO2: {emissions:.6f} kg")

def benchmark_model(model_name, input_data, iterations=100):
    """
    Executes a benchmark with Warm-up.
    
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = get_model(model_name).to(device)
    model.eval()
    device = next(model.parameters()).device
    
    # 1. Warm-up Phase (Critical for GPU)

    with torch.no_grad():
        for _ in range(10):
            _ = model(input_data)
    
    # 2. Measurement Phase
    with GreenProfiler(model_name, device=str(device)) as prof:
        with torch.no_grad():
            for _ in range(iterations):
                _ = model(input_data)
                
    return prof