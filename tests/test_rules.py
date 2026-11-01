from weather_alert.rules import build_alerts

def test_no_alerts_on_calm_day():
    assert build_alerts({"rain": 0, "max_temp": 25, "wind": 10}) == []

def test_rain_alert():
    alerts = build_alerts({"rain": 12, "max_temp": 25, "wind": 10})
    assert len(alerts) == 1 and "rain" in alerts[0].lower()