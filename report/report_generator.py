def generate_report(values, anomalies):
    report = []
    report.append(f"Минимална осветеност: {min(values)}")
    report.append(f"Максимална осветеност: {max(values)}")
    report.append(f"Средна осветеност: {sum(values)/len(values):.2f}")
    report.append(f"Брой аномалии: {sum(anomalies)}")
    report.append("\nЗаключение:")

    if sum(anomalies) > 5:
        report.append("Наблюдават се чести резки промени в осветеността.")
    else:
        report.append("Осветеността е сравнително стабилна.")

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report))
