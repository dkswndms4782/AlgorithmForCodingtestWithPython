def chk(n):
    Num = 1
    count = 1
    while Num % n != 0:
        Num = (Num * 10 + 1) % n
        count += 1
    return count


while True:
    try:
        n = int(input())
        print("{}".format(chk(n)))
    except EOFError:
        break
