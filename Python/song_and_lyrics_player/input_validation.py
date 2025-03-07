from utils import STYLE


def get_video_id(previous_id: str) -> str:
    while True:
        video_id = input(f"Enter the YouTube video ID [previous: {previous_id}]: ")

        if not video_id:
            return previous_id
        
        if len(video_id) == 11:
            return video_id
        else:
            print(STYLE["YELLOW"] + "⚠️  Invalid video ID. Enter a valid video ID." + STYLE["RESET"])


def get_coloured_text_preference(default_value: bool) -> bool:
    while True:
        coloured_text = input(f"Use coloured text? (Y/N) [default: {default_value}]: ")

        if not coloured_text:
            return default_value
        
        if coloured_text.upper() in ["Y", "N"]:
            return coloured_text.upper() == "Y"
        else:
            print(STYLE["YELLOW"] + "⚠️  Invalid input. Enter 'Y' or 'N'." + STYLE["RESET"])


def get_volume(default_volume: float) -> float:
    while True:
        volume_input = input(f"Volume (0.0 to 1.0) [default: {default_volume}]: ")

        if not volume_input:
            return default_volume
        
        try:
            volume = float(volume_input)
            if 0.0 <= volume <= 1.0:
                return volume
            else:
                print(STYLE["YELLOW"] + "⚠️  Volume must be between 0.0 and 1.0" + STYLE["RESET"])
        except ValueError:
            print(STYLE["YELLOW"] + "⚠️  Invalid input. Enter a number between 0.0 and 1.0." + STYLE["RESET"])

