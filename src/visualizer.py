import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class GreenVisualizer:
    """
    Professional plotting suite for Environmental AI metrics.
    """
    def __init__(self, output_dir="reports/figures"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        # Set a professional style
        sns.set_theme(style="whitegrid")
        plt.rcParams['figure.dpi'] = 300 # High resolution for PFE print

    def plot_energy_vs_latency(self, summary_df):
        """
        Creates a scatter plot comparing Energy vs. Latency.
        """
        plt.figure(figsize=(10, 6))
        
        # We use 'energy_consumed' on Y and 'duration' on X
        plot = sns.scatterplot(
            data=summary_df,
            x='duration',
            y='energy_consumed',
            hue='project_name',
            s=100, # Point size
            palette='viridis'
        )

        plt.title("The Green Frontier: Energy vs. Latency", fontsize=15, pad=20)
        plt.xlabel("Average Latency (seconds)", fontsize=12)
        plt.ylabel("Energy Consumed (Wh)", fontsize=12)
        
        # Annotate each point with the model name
        for i in range(summary_df.shape[0]):
            plt.text(
                summary_df.duration[i], 
                summary_df.energy_consumed[i] + 0.000001, # Offset
                summary_df.project_name[i],
                fontsize=9
            )

        plt.tight_layout()
        save_path = os.path.join(self.output_dir, "energy_latency_tradeoff.png")
        plt.savefig(save_path)
        print(f"--- Chart saved to: {save_path}")
        plt.close()

    def plot_carbon_footprint(self, summary_df):
        """
        Creates a bar chart showing CO2 emissions per model.
        """
        plt.figure(figsize=(8, 5))
        sns.barplot(
            data=summary_df,
            x='project_name',
            y='emissions',
            palette='magma'
        )
        
        plt.title("Carbon Footprint per Model (CO2eq)", fontsize=14)
        plt.ylabel("Emissions (kg CO2eq)")
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        save_path = os.path.join(self.output_dir, "carbon_footprint.png")
        plt.savefig(save_path)
        plt.close()