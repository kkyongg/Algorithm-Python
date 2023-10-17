# 실습1 : len() 사용하지 않고 구현
def my_len(x):
    length = 0
    for i in x:
        length += 1
    return length


a = [5, 5, 6, 7, 8, 3]
b = 'Life is short.'

# 내장 함수 len() 
print(len(a), len(b)) # 6 14
# my_len()
print(my_len(a), my_len(b)) # 6 14 

# 실습2 : 양의 정수 a와 b를 전달받아 a부터 b까지 곱해서 반환하는 mult 함수 작성
def mult(a, b):
    result = 1
    for i in range(a, b+1, 1):
        result *= i
    return result


print(mult(1, 3)) # 6
print(mult(2, 5)) # 120

# 실습3 : 숫자로 구성된 리스트를 전달받아, 리스트에서 양수 값을 더한 결과와 음수 값을 더한 결과를 반환하는 함수 작성
def sum_pos_neg(l):
    pos = 0
    neg = 0
    for i in l:
        if i > 0:
            pos += i
        else:
            neg += i

    return pos, neg


possum, negsum = sum_pos_neg([3, 4, -6, -3])
print(possum, negsum) # 7 -9

mylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]
possum2, negsum2 = sum_pos_neg(mylist)
print(possum2, negsum2) # 1 -1

# 실습4 : 1개 이상의 2차원 벡터들을 전달받아 벡터들의 합을 구하여 반환하는 함수 작성
def vector_sum(vector, *vectors):
    result = list(vector)

    for v in vectors:
        result[0] += v[0]
        result[1] += v[1]
    return result


v1 = [0, 1]
v2 = [0.5, 0.5]
v3 = [1, 0]
v4 = [6, 4]
v5 = [3.13, 2.72]

m1 = vector_sum(v1, v2, v3)
m2 = vector_sum(v1, v2, v3, v4)
m3 = vector_sum(v3, v5)

print(m1, m2, m3) # [1.5, 1.5] [7.5, 5.5] [4.13, 2.72]

# 실습5 : 숫자로 구성된 리스트 2개를 받아서 이 두 리스트를 합친 후에 정렬한 새로운 리스트를 반환하는 함수 작성
# 단, 매개변수의 값이 주어지지 않으면, [0]이 기본적으로 주어짐
def merge_list(l1=[0], l2=[0]):
    result = []

    for i in l1:
        result.append(i)

    for j in l2:
        result.append(j)

    result = sorted(result)
    return result


l = [3, 5, 9, 1, 2]

ml1 = merge_list(l, [2, 1])
ml2 = merge_list([6, 9, 4])
ml3 = merge_list()

print(ml1) # [1, 1, 2, 2, 3, 5, 9]
print(ml2) # [0, 4, 6, 9]
print(ml3) # [0, 0]