def extended_euclidean(a, b):
    # Initialize variables
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    # Apply the Euclidean algorithm with back substitution to find the coefficients u and v
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # At the end, old_r is the gcd and old_s and old_t are the coefficients (u and v)
    return old_s, old_t


# Example: p = 26513, q = 32321
p = 26513
q = 32321

u, v = extended_euclidean(p, q)

# Print the result
print(f"u = {u}, v = {v}")
