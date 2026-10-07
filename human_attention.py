import json
from pathlib import Path
from datetime import datetime

ALERT_FILE = Path(__file__).parent / "human_attention.json"


def flag_human_attention(reason, priority="high"):
    alerts = get_alerts()

    alert = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M"),
        "reason": reason,
        "priority": priority,
        "status": "open"
    }

    alerts.append(alert)

    with open(ALERT_FILE, "w", encoding="utf-8") as f:
        json.dump(alerts, f, indent=2)

    return alert


def get_alerts():
    if not ALERT_FILE.exists():
        return []

    with open(ALERT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)