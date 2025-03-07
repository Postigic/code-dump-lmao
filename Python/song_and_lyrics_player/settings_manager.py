import json


def save_settings(video_id: str, coloured_text: bool, volume: float, filename: str) -> None:
    settings = {
        "video_id": video_id,
        "coloured_text": coloured_text,
        "volume": volume,
    }
    with open(filename, 'w') as f:
        json.dump(settings, f)


def load_settings(filename: str) -> dict:
    if not filename.exists():
        return {"video_id": None, "coloured_text": True, "volume": 0.65}
    with open(filename, 'r') as file:
        settings = json.load(file)
    return settings
