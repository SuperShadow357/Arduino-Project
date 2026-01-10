import csv
from datetime import datetime

class CSVLogger:
    def __init__(self, filename="data.csv"):
        self.filename = filename
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "raw", "smoothed", "anomaly"])

    def log(self, raw, smoothed, anomaly):
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                raw,
                round(smoothed, 2) if smoothed else None,
                anomaly
            ])
