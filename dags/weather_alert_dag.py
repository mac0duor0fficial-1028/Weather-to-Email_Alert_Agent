import sys
from datetime import datetime, timedelta
from pathlib import Path

from airflow.decorators import dag, task

# Make src/ importable inside Airflow
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from weather_alert import config
from weather_alert.weather import get_forecast
from weather_alert.rules import build_alerts
from weather_alert.notifier import send_email

default_args = {
    "owner": "you",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    dag_id="weather_alert",
    description="Fetch forecast, check rules, email alerts",
    schedule="0 6 * * *",              # daily at 6 AM
    start_date=datetime(2025, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=["weather", "alerts"],
)
def weather_alert_pipeline():

    @task
    def fetch_weather() -> dict:
        return get_forecast()

    @task
    def check_rules(weather: dict) -> list[str]:
        return build_alerts(weather)

    @task
    def send_alert(alerts: list[str]) -> str:
        if not alerts:
            return "No alerts today."
        body = f"Weather alert for {config.CITY}:\n\n" + "\n".join(alerts)
        send_email(f" Weather Alert: {config.CITY}", body)
        return "Alert sent."

    send_alert(check_rules(fetch_weather()))


weather_alert_pipeline()