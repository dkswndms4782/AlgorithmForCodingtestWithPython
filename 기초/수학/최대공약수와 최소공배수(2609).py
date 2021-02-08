def GCD(a, b):
    if not a % b:
        return b
    return GCD(b, a % b)


a, b = map(int, input().split())
if a > b:
    print("{}\n{}".format(GCD(a, b), a * b // GCD(a, b)))
else:
    print("{}\n{}".format(GCD(b, a), a * b // GCD(b, a)))
