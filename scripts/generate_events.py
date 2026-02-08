import csv
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

NUM_EVENTS = 1000
OUTPUT_DIR = Path("data/raw")
CSV_FILE = OUTPUT_DIR / "events.csv"
JSON_FILE = OUTPUT_DIR / "events.json"

EVENT_TYPES = ["click", "view", "add_to_cart", "purchase", "logout"]
DEVICES = ["mobile", "desktop", "tablet"]
LOCATIONS = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Pune"]


def random_timestamp(days_back=7):
    now = datetime.now()
    delta = timedelta(
        days=random.randint(0, days_back),
        seconds=random.randint(0, 86400)
    )
    return (now - delta).isoformat(timespec="seconds")


def generate_event(event_id):
    return {
        "event_id": event_id,
        "user_id": f"user_{random.randint(1, 300)}",
        "event_type": random.choice(EVENT_TYPES),
        "timestamp": random_timestamp(),
        "device": random.choice(DEVICES),
        "location": random.choice(LOCATIONS)
    }


def write_csv(events):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=events[0].keys())
        writer.writeheader()
        writer.writerows(events)


def write_json(events):
    with open(JSON_FILE, mode="w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    events = [generate_event(i) for i in range(1, NUM_EVENTS + 1)]

    write_csv(events)
    write_json(events)

    print(f"Generated {NUM_EVENTS} events")
    print(f"CSV saved to: {CSV_FILE}")
    print(f"JSON saved to: {JSON_FILE}")


if __name__ == "__main__":
    main()
