from . import config
from .weather import get_forecast
from .rules import build_alerts
from .notifier import send_email

def run() -> None:
    weather = get_forecast()
    alerts = build_alerts(weather)

    if alerts:
        body = f"Weather alert for {config.CITY}:\n\n" + "\n".join(alerts)
        send_email(f" Weather Alert: {config.CITY}", body)
        print("Alert sent.")
    else:
        print("No alerts today.", weather)

if __name__ == "__main__":
    run()