a, b, c, = map(int, input().split())


# 모두 같은 눈
if a == b and a == c:
    print(10000+(a*1000))
# 2개가 같은 눈
elif a == b:
    print(1000+(a*100))
elif b == c:
    print(1000+(b*100))
elif a == c:
    print(1000+(a*100))
# 모두 다른 눈
else :
    print(100 * max(a,b,c)) 