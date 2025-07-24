light_mapping = {
    "R": 0,
    "G": 0,
    "B": 1,
    "Y": 2,
    "W": 3
}

display_mapping = {
    "R": 1,
    "G": 3,
    "B": 2,
    "Y": 3,
    "W": 4
}

def colours_to_num(light_colours, display_colours):
    display_sum = sum(display_mapping[colour] for colour in display_colours)
    light_sum = sum(light_mapping[colour] for colour in light_colours)
    result = display_sum - light_sum
    return result if result > 0 else 0
