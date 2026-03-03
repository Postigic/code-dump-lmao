import random
from utils import format, superscript
from dataclasses import dataclass, field

_BINARY = ["add", "sub", "mul", "div"]
_UNARY  = ["add", "sub", "sqrt", "cbrt", "pow"]

# trust me, i don't understand what i'm doing here either

@dataclass
class Node:
    op: str
    value: float
    children: list = field(default_factory=list)

def generate(num: float) -> str:
    depth = random.randint(2, 5)
    tree = _build(num, depth)

    return _render(tree)

def _build(num: float, depth: int) -> Node:
    if depth <= 1:
        pool = [s for s in _UNARY if _applicable(s, num)]

        if not pool:
            pool = ["sub"]
        
        return Node(op=random.choice(pool), value=num)
    
    pool = [s for s in _BINARY if _applicable(s, num)]
    op = random.choice(pool)
    lv, rv = _split(num, op)

    return Node(op=op, value=num, children=[_build(lv, random.randint(1, depth - 1)), _build(rv, random.randint(1, depth - 1))])

def _split(num: float, op: str) -> tuple[float, float]:
    if op == "add":
        if num == 0:
            a = random.randint(1, 10)
            return (a, a)
        
        a = random.randint(1, abs(num) - 1) if abs(num) > 1 else abs(num)
        a *= 1 if num > 0 else -1
        
        return (a, num - a)
    elif op == "sub":
        if num == 0:
            a = random.randint(1, 10)
            return (a, a)
        
        a = (abs(num) + random.randint(1, abs(num) + 10)) * (1 if num > 0 else -1)

        return (a, a - num)
    elif op == "mul":
        divisors = [a for a in range(2, 13) if num % a == 0]
        a = random.choice(divisors)

        return (a, num // a)
    elif op == "div":
        a = random.randint(2, 12)

        return (num * a, a)

def _render(node: Node) -> str:
    if not node.children:
        v = node.value
        op = node.op

        if op == "sqrt":
            return f"√({format(v ** 2)})"
        elif op == "cbrt":
            return f"∛({format(v ** 3)})"
        elif op == "pow":
            for exp in range(2, 5):
                if round(v ** (1 / exp)) ** exp == v:
                    return f"{format(round(v ** (1 / exp)))}{superscript(exp)}"
        elif op == "add":
            a = random.randint(1, abs(v) - 1) if abs(v) > 1 else abs(v)
            a *= 1 if v >= 0 else -1
            b = v - a

            return f"{format(a)} + {format(b)}"
        elif op == "sub":
            a = (abs(v) + random.randint(1, abs(v) + 10)) * (1 if v >= 0 else -1)
            b = a - v

            return f"{format(a)} - {format(abs(b))}"
        
    lc, rc = node.children
    l = _render(lc)
    r = _render(rc)
    rv = rc.value

    lp = f"({l})"
    rp = f"({r})"

    op = node.op

    if op == "add":
        if rv < 0:
            return f"{lp} - ({_render_abs(rc)})"
        
        return f"{lp} + {rp}"
    elif op == "sub":
        if rv < 0:
            return f"{lp} + ({_render_abs(rc)})"
        
        return f"{lp} - {rp}"
    elif op == "mul":
        return f"{lp} × {rp}"
    elif op == "div":
        return f"{lp} ÷ {rp}"

def _render_abs(node: Node) -> str:
    flipped = Node(op=node.op, value=abs(node.value), children=[Node(op=c.op, value=abs(c.value), children=c.children) for c in node.children])

    return _render(flipped)

def _applicable(op: str, num: float) -> bool:
    if op == "add" and abs(num) <= 1: return False
    if op == "sub" and abs(num) <= 1: return False
    if op == "mul" and not any(num % a == 0 for a in range(2, 13)): return False
    if op == "div" and num == 0: return False
    if op == "pow" and (num <= 1 or not any(round(num ** (1 / exp)) ** exp == num for exp in range(2, 5))): return False
    if op == "sqrt" and num <= 1: return False
    if op == "cbrt" and num <= 1: return False

    return True
