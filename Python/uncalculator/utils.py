_SUPERSCRIPTS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
_SUBSCRIPTS = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

def format(num: float) -> str:     
    if num == int(num):
        return str(int(num))
    
    return str(num)

def superscript(num: int) -> str:
    return str(num).translate(_SUPERSCRIPTS)

def subscript(num: int) -> str:
    return str(num).translate(_SUBSCRIPTS)
