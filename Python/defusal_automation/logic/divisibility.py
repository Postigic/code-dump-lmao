def number_to_button(num: int) -> str:
    div_by_2 = num % 2 == 0
    div_by_3 = num % 3 == 0
    div_by_5 = num % 5 == 0
    div_by_7 = num % 7 == 0

    key = (div_by_2, div_by_3, div_by_5, div_by_7)

    mapping = {
        (True, False, True, True): "A",
        (False, True, True, True): "A",
        (True, False, False, False): "A",
        (False, True, False, True): "B",
        (True, True, False, False): "B",
        (False, True, True, False): "B",
        (True, True, True, False): "C",
        (True, True, False, True): "C",
        (False, False, False, True): "C",
        (True, True, True, True): "D",
        (False, True, False, False): "D",
        (True, False, False, True): "E",
        (False, False, True, True): "E",
        (True, False, True, False): "E",
        (False, False, True, False): "F",
        (False, False, False, False): "F",
    }

    return mapping.get(key)
