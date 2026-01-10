import matplotlib.pyplot as plt

class LivePlot:
    def __init__(self):
        self.values = []
        self.anomalies = []

        plt.ion()
        self.fig, self.ax = plt.subplots()

    def update(self, value, anomaly):
        self.values.append(value)
        self.anomalies.append(anomaly)

        self.ax.clear()
        self.ax.plot(self.values, label="Осветеност")

        for i, a in enumerate(self.anomalies):
            if a:
                self.ax.scatter(i, self.values[i])

        self.ax.set_title("Осветеност в реално време")
        self.ax.set_ylabel("Стойност (0–1023)")
        self.ax.legend()
        plt.pause(0.01)
