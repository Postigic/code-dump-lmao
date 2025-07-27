import sys

n = int(sys.stdin.readline().strip())
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False

print(" ".join(str(i) for i in range(2, n + 1) if is_prime[i]))

"""
Why must any composite number n <= n must have a factor <= sqrt(n)?

What is a compsoite number?
A composite number is a number that can be factored into two integers:
n = a * b, where a and b are both > 1 and != n.

Let's say a > sqrt(n) and b > sqrt(n).
Using the definition of composite numbers, we can see that:
a * b > sqrt(n) * sqrt(n) = n.
However, this would mean that n > n, which is a contradiction.
So both factors cannot be greater than sqrt(n).

Therefore, at least one factor must be less than or equal to sqrt(n).
"""
