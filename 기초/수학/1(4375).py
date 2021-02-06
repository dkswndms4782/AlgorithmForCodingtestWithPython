import sys


def chk(n):
    Num = 1
    count = 1
    while Num % n != 0:
        Num = (Num * 10 + 1) % n
        count += 1
    return count


def input():
    return sys.stdin.readline().rstrip()


# python에서 input은 굉장히 느리기 때문에 속도를 향상시키기 위해서 사용하는 문장
# def input(): return sys.stdin.readline().rstrip()
while True:
    try:
        n = int(input())
        print("{}".format(chk(n)))
    except EOFError:
        break

# while True:
#     try:
#         # 실행할 구문
#     except EOFError:
#         break
# 1. sys 모듈을 import 하여 sys.stdin.readlines()로 EOF까지 자동으로 읽어오도록 만들어서 출력하는 방법

# 2. try-catch 문으로 구성하고 EOFError가 발생하면 반복문을 탈출하는 방법
