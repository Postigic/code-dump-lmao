import numpy as np
from sympy import Eq, linear_eq_to_matrix
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy.polys.polyerrors import PolynomialError
from utils import STYLE

transformations = standard_transformations + (implicit_multiplication_application,)
        
def parse_equation(prompt: str) -> tuple:
    equations = []

    print(STYLE["CYAN"] + "\nEnter each linear equation (e.g., 2x + 3y = 5). Variables are case-sensitive. Type 'done' when finished." + STYLE["RESET"])

    while True:
        raw_eq = input(prompt).strip().replace(" ", "")

        if raw_eq.lower() == "done":
            if not equations:
                print(STYLE["RED"] + f"At least 2 linear equations required. Currently {len(equations)} entered." + STYLE["RESET"])
                continue
            break

        if not raw_eq or "=" not in raw_eq:
            print(STYLE["RED"] + "Invalid equation format. Please enter a valid equation." + STYLE["RESET"])
            continue

        try:
            lhs, rhs = raw_eq.split("=")

            lhs = parse_expr(lhs, transformations=transformations, evaluate=False)
            rhs = parse_expr(rhs, transformations=transformations, evaluate=False)

            eq = Eq(lhs, rhs)

            free_syms = list(eq.free_symbols)

            A_test, B_test = linear_eq_to_matrix([eq], free_syms)
            if A_test.shape[1] != len(free_syms):
                raise PolynomialError("Non-linear term detected.")
            
            equations.append(eq)
        except (PolynomialError, ValueError, TypeError) as e:
            print(STYLE["RED"] + f"Non-linear or invalid equation: {raw_eq}. Please re-enter." + STYLE["RESET"])
        except Exception as e:
            print(STYLE["RED"] + f"Error: {e}. Please re-enter." + STYLE["RESET"])

    all_symbols = sorted(set().union(*(eq.free_symbols for eq in equations)), key=lambda s: s.name)

    try:
        A_sym, B_sym = linear_eq_to_matrix(equations, all_symbols)
        A = np.array(A_sym, dtype=np.float64)
        B = np.array(B_sym, dtype=np.float64)
    except Exception as e:
        print(STYLE["RED"] + f"Matrix error: {e}" + STYLE["RESET"])
        return None, None, None

    return A, B, all_symbols
