def numbers_to_sequence(number_string):
    num1, num2, num3, num4, num5, num6 = map(int, number_string)

    all_colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]

    initial_colors = ["Red" if num1 < 6 else "Orange",
                      "Yellow" if num2 < 6 else "Green",
                      "Blue" if num3 < 6 else "Purple"]

    for colour in initial_colors:
        all_colours.remove(colour)

    remaining_colors = [all_colours[1], all_colours[2], all_colours[0]] if num4 < 7 else \
                       [all_colours[2], all_colours[1], all_colours[0]] if num5 < 7 else \
                       [all_colours[0], all_colours[1], all_colours[2]] if num6 > 5 else \
                       [all_colours[0], all_colours[2], all_colours[1]]

    colour_sequence = initial_colors + remaining_colors

    return ", ".join(colour_sequence)
