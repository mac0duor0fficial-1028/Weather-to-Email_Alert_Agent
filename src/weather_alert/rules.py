from . import config

def build_alerts(w: dict) -> list[str]:
    alerts = []
    if w["rain"] >= config.RAIN_THRESHOLD_MM:
        alerts.append(f" Heavy rain expected: {w['rain']} mm")
    if w["max_temp"] >= config.HEAT_THRESHOLD_C:
        alerts.append(f" High temperature: {w['max_temp']}°C")
    if w["wind"] >= config.WIND_THRESHOLD_KMH:
        alerts.append(f" Strong wind: {w['wind']} km/h")
    return alerts