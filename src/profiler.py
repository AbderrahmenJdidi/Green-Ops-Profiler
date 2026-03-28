import time
import torch
from codecarbon import EmissionsTracker

class GreenProfiler:
    """
    A Professional Context Manager for AI Energy Benchmarking.
    """
    def __init__(self, model_name, device="cpu"):
        self.model_name = model_name
        self.device = device
        # Initialize CodeCarbon in 'offline' mode to avoid network
        self.tracker = EmissionsTracker(measure_power_secs=1, save_to_file=True, log_level='error')

    def __enter__(self):
        print(f" [START] Profiling: {self.model_name} on {self.device}")
        self.start_time = time.perf_counter()
        self.tracker.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        emissions = self.tracker.stop()
        self.end_time = time.perf_counter()
        
        duration = self.end_time - self.start_time
        print(f" [FINISH] {self.model_name} | Duration: {duration:.2f}s | CO2: {emissions:.6f} kg")

def benchmark_model(model, input_data, iterations=100):
    """
    Executes a benchmark with Warm-up.
    """
    model.eval()
    device = next(model.parameters()).device
    
    # 1. Warm-up Phase (Critical for GPU)

    with torch.no_grad():
        for _ in range(10):
            _ = model(input_data)
    
    # 2. Measurement Phase
    with GreenProfiler(model.__class__.__name__, device=str(device)) as prof:
        with torch.no_grad():
            for _ in range(iterations):
                _ = model(input_data)
                
    return prof