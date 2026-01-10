import json
import time

from serial_reader.arduino_reader import ArduinoReader
from processing.validator import validate_light
from processing.smoothing import moving_average
from processing.anomaly import is_anomaly
from storage.logger import CSVLogger
from visualization.plotter import LivePlot
from report.report_generator import generate_report

# Зареждане на конфигурация
with open("config.json") as f:
    config = json.load(f)

reader = ArduinoReader(config["serial_port"], config["baud_rate"])
reader.connect()

logger = CSVLogger()
plot = LivePlot()

values = []
anomalies = []
previous = None

try:
    while True:
        raw = reader.read_value()

        if validate_light(raw):
            values.append(raw)
            smooth = moving_average(values, config["moving_average_window"])
            anomaly = is_anomaly(raw, previous, config)

            anomalies.append(anomaly)
            logger.log(raw, smooth, anomaly)
            plot.update(raw, anomaly)

            previous = raw

        time.sleep(config["interval_seconds"])

except KeyboardInterrupt:
    print("\nСпиране...")
    generate_report(values, anomalies)
    reader.close()
