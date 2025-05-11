import numpy as np
from input_handler import parse_equation
from utils import STYLE

def solve_linear_system(A, B, all_symbols):
    if A.shape[0] != A.shape[1]:
        print(STYLE["RED"] + f"\nRequire {A.shape[1]} variables but got {A.shape[0]} equations. No unique solution." + STYLE["RESET"])
        return
    
    try:
        solution = np.linalg.solve(A, B)
        print(STYLE["MAGENTA"] + "\nSolution:" + STYLE["RESET"])

        for sym, val in zip(all_symbols, solution):
            num = val[0]
            formatted = round(num, 6) if not np.isclose(num, round(num)) else int(round(num))
            print(STYLE["GREEN"] + f"{sym} = {formatted}" + STYLE["RESET"])    
    except np.linalg.LinAlgError:
        aug = np.hstack((A, B.reshape(-1, 1)))
        rank_A = np.linalg.matrix_rank(A)
        rank_aug = np.linalg.matrix_rank(aug)

        if rank_A != rank_aug:
            msg = "Inconsistent system: No solution exists."
        else:
            msg = "Infinitely many solutions (dependent system)."
        
        print(STYLE["RED"] + f"\n{msg}" + STYLE["RESET"])


def main():
    print(STYLE["YELLOW"] + "Linear System Solver" + STYLE["RESET"])

    while True:
        A, B, symbols = parse_equation("Enter equation: ")

        if A is not None:
            solve_linear_system(A, B, symbols)

        if input(STYLE["CYAN"] + "\nSolve another? (Y/N): " + STYLE["RESET"]).upper() != "Y":
            break

if __name__ == "__main__":
    main()
