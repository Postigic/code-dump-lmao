def extended_euclidean(a, b):
    old_r, r = a, b
    old_u, u = 1, 0
    old_v, v = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_u, u = u, old_u - quotient * u
        old_v, v = v, old_v - quotient * v

    return old_u, old_v

p = 26513
q = 32321

u, v = extended_euclidean(p, q)

print(f"u = {u}, v = {v}")
