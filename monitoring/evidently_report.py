
import pandas as pd
from pathlib import Path
from evidently import Report
from evidently.presets import DataDriftPreset


def generate_report():

    # Previous/reference addition data
    reference_data = pd.DataFrame({
        "number1": [10 + i for i in range(100)],
        "number2": [20 + i for i in range(100)],
        "result": [30 + 2 * i for i in range(100)]
    })

    # New/current addition data
    current_data = pd.DataFrame({
        "number1": [100 + i for i in range(100)],
        "number2": [200 + i for i in range(100)],
        "result": [300 + 2 * i for i in range(100)]
    })

    report = Report([
        DataDriftPreset()
    ])

    snapshot = report.run(
        current_data,
        reference_data
    )

    # Create reports folder
    output_folder = Path("reports")
    output_folder.mkdir(exist_ok=True)

    snapshot.save_html(
        str(output_folder / "evidently_report.html")
    )

    print("Evidently report generated successfully!")


if __name__ == "__main__":
    generate_report()
