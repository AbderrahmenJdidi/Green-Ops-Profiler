# Green-Ops Profiler v1.1

> **"Turning the invisible environmental cost of AI into actionable engineering data."**

Green-Ops is a telemetry suite designed to audit the energy consumption, carbon footprint, and latency of Deep Learning models. By integrating hardware-aware monitoring with Dockerized environments, it ensures scientific reproducibility for sustainable AI research.

## Key Features
- **Hardware-Aware Telemetry:** Real-time tracking of CPU/GPU wattage and CO2eq emissions using CodeCarbon.
- **Session-Aware Reporting:** Smart temporal filtering that isolates current experiments from historical logs.
- **Reproducible Infrastructure:** Fully containerized via Docker to eliminate "dependency hell" and ensure environment parity.
- **The Green Frontier:** Automated generation of high-resolution (300 DPI) Pareto Front visualizations (Energy vs. Latency).

## Tech Stack
- **Engine:** PyTorch (Inference & Architecture management)
- **Monitoring:** CodeCarbon, pynvml (GPU metrics), psutil (CPU metrics)
- **Data Engineering:** Pandas (Aggregation), Matplotlib/Seaborn (Visualization)
- **Deployment:** Docker (Standardized Environment)

## Quick Start
1. **Clone & Setup:**
   ```bash
   python -m venv env
   source env/bin/activate  # or .\env\Scripts\activate on Windows
   pip install -r requirements.txt
2. **Run Audit:**
   ```bash
   python main.py
3. **Docker Deployment:**
   ```bash
   docker build -t green-ops-profiler .
   docker run --gpus all green-ops-profiler


## OUTPUTS 
**emissions.csv:** Comprehensive historical hardware logs.
**reports/summary_report.csv:** Aggregated session metrics.
**reports/figures/:** Publication-quality performance charts.