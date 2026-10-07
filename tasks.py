import json
from pathlib import Path

TASK_FILE = Path(__file__).parent / "care_tasks.json"


def create_task(task):
    tasks = get_tasks()

    tasks.append({
        "task": task,
        "status": "pending"
    })

    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

    return tasks[-1]


def get_tasks():
    if not TASK_FILE.exists():
        return []

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)