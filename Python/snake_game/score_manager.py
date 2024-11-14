import json
from pathlib import Path

json_file_path = Path(__file__).parent / "high_score.json"


def load_high_score():
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)
            return data.get("high_score", 0)
    except FileNotFoundError:
        return 0


def save_high_score(high_score):
    with open(json_file_path, "w") as file:
        json.dump({"high_score": high_score}, file)
