def bin_search_sqrt(n):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")
    if n == 0 or n == 1:
        return n
    
    low, high = 0, n
    res = 0

    while low <= high:
        mid = low + (high - low) // 2
        mid_squared = mid * mid
        
        if mid_squared == n:
            return mid
        elif mid_squared < n:
            res = mid
            low = mid + 1
        else:
            high = mid - 1

    return res

results = [
    bin_search_sqrt(25),
    bin_search_sqrt(10),
    bin_search_sqrt(0),
    bin_search_sqrt(1),
    bin_search_sqrt(16),
    bin_search_sqrt(100),
    bin_search_sqrt(50),
]

print(*results, sep="\n")
