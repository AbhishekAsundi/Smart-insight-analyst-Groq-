import os
import matplotlib.pyplot as plt

class VisualizationAgent:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, df):
        charts = []

        # Top-N Bar Chart for categorical data
        cat_cols = df.select_dtypes(include=["object"]).columns
        if len(cat_cols) > 0:
            col = cat_cols[0]
            top_n = df[col].value_counts().nlargest(10)
            plt.figure(figsize=(8, 5))
            top_n.plot(kind="bar", color="skyblue")
            plt.title(f"Top 10 Categories in '{col}'")
            plt.ylabel("Count")
            plt.xlabel(col)
            cat_path = os.path.join(self.output_dir, f"{col}_top10_bar.png")
            plt.tight_layout()
            plt.savefig(cat_path)
            plt.close()
            charts.append(cat_path)

        # Histogram for numeric data
        num_cols = df.select_dtypes(include=["number"]).columns
        if len(num_cols) > 0:
            col = num_cols[0]
            plt.figure(figsize=(8, 5))
            df[col].hist(bins=30, color="orange", edgecolor="black")
            plt.title(f"Histogram of '{col}'")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            hist_path = os.path.join(self.output_dir, f"{col}_hist.png")
            plt.tight_layout()
            plt.savefig(hist_path)
            plt.close()
            charts.append(hist_path)

        return charts
