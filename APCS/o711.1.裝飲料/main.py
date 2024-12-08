n = int(input())
w1, w2, h1, h2 = map(int, input().split())
nums = map(int, input().split())

hs = []

sq1 = w1 * w1
sq2 = w2 * w2

isbox1fill = False
isbox2fill = False

for num in nums:
    # 每次新增的
    increase = 0

    # 下面盒子未滿情況下
    if not isbox1fill:
        if num // sq1 > h1:
            increase += h1
            isbox1fill = True
            num -= sq1 * h1
        else:
            h1 = h1 - num // sq1
            increase += num // sq1

    # 下面盒子滿了，且上方未滿
    if isbox1fill and not isbox2fill:
        if num // sq2 > h2:
            increase += h2
            isbox2fill = True
            num -= sq2 * h2
        else:
            h2 = h2 - num // sq2
            increase += num // sq2

    hs.append(increase)

print(max(hs))
