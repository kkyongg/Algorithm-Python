total = int(input())  # 총 금액
goods = int(input())  # 구매한 물건의 종류의 수

sum = 0
for i in range(goods):
    price, good = map(int, input().split())
    sum += price * good

if total == sum:
    print("Yes")
else:
    print("No")
