import os

# ---- Location ----
LAT = float(os.getenv("LAT", "-1.29"))
LON = float(os.getenv("LON", "36.82"))
CITY = os.getenv("CITY", "Nairobi")

# ---- Alert thresholds ----
RAIN_THRESHOLD_MM = float(os.getenv("RAIN_THRESHOLD_MM", "5"))
HEAT_THRESHOLD_C = float(os.getenv("HEAT_THRESHOLD_C", "33"))
WIND_THRESHOLD_KMH = float(os.getenv("WIND_THRESHOLD_KMH", "40"))

# ---- SMTP ----
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))


def require(name: str) -> str:
    """Return a required setting, or fail with a clear message."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value