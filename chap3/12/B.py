N = int(input())


def calc_error(x: float):
    y = x**3 + x
    abs_error = abs(y - N)
    rel_error = abs_error / N

    return y, min(abs_error, rel_error)


left = 0
right = 100

while left < right:
    mid = (left + right) / 2
    y, error = calc_error(mid)

    if error <= 0.001:
        print(mid)
        exit(0)
    elif y > N:
        right = mid
    else:
        left = mid
