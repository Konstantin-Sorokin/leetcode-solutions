def climb_stairs(n: int) -> int:
    if n < 3:
        return n

    i, j = 1, 2

    for _ in range(n - 2):
        i, j = j, i + j

    return j


print(climb_stairs(5))
print(climb_stairs(44))