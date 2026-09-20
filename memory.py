import json
from pathlib import Path

MEMORY_FILE = Path(__file__).parent / "care_memory.json"


def save_memory(observation):
    memory = []

    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)

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