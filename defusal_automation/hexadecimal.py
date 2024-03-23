def hex_to_alpha(hex_string):
    return "".join(chr(int(pair, 16)) for pair in hex_string.split())
