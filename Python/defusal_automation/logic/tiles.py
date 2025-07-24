colour_mapping = {
    "R": 1,
    "G": 9,
    "B": 7,
    "Y": 2,
    "P": 6,
    "W": 5
}

def tiles_to_num(colour_string):
    return sum(colour_mapping[colour] for colour in colour_string)
