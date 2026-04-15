# i don't know why i can't fully understand this algorithm :(
def tournament_sort(state):
    arr = state.arr
    n = len(arr)

    size = 1
    while size < n:
        size <<= 1
    
    leaves = arr + [float("inf")] * (size - n)
    tree = [0] * (2 * size)

    for i in range(size):
        tree[size + i] = i

    for i in range(size - 1, 0, -1):
        l, r = tree[2 * i], tree[2 * i + 1]

        state.active = {l for l in {tree[2*i], tree[2*i+1]} if l < n}
        yield

        tree[i] = l if leaves[l] <= leaves[r] else r

    state.active.clear()
    yield

    for pos in range(n):
        winner = tree[1]
        arr[pos] = leaves[winner]

        state.sorted_.add(pos)
        yield

        leaves[winner] = float("inf")

        i = (size + winner) // 2
        while i >= 1:
            l, r = tree[2 * i], tree[2 * i + 1]

            state.active = {l for l in {tree[2*i], tree[2*i+1]} if l < n}
            yield

            tree[i] = l if leaves[l] <= leaves[r] else r
            i //= 2

        state.active.clear()
        yield
