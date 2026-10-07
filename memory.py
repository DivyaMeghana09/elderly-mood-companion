import json
from pathlib import Path
from datetime import datetime

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

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M"),
        "observation": observation,
        "mood": mood
    }

    memory.append(entry)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

    return entry