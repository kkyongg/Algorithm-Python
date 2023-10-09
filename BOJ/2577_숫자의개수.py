A = int(input())
B = int(input())
C = int(input())

answer = A * B * C
result = list(str(answer))

for i in range(10):
    print(result.count(str(i)))