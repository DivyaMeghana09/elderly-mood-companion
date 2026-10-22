import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

MEMORY_FILE = Path(__file__).parent / "care_memory.json"


def save_memory(observation):
    memory = get_memories()

    memory.append({
        "observation": observation
    })

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)


def get_memories():
    if not MEMORY_FILE.exists():
        return []

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def update_timeline(observation, mood=""):
    memory = get_memories()

    # Use India Standard Time (IST)
    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    entry = {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M"),
        "observation": observation,
        "mood": mood
    }

    memory.append(entry)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

    return entry
