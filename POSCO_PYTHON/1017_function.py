# 실습1
def my_len(x):
    length = 0
    for i in x:
        length += 1
    return length


a = [5, 5, 6, 7, 8, 3]
b = 'Life is short.'

print(len(a), len(b))  # 내장 함수 len()
print(my_len(a), my_len(b))  # my_len()

# 실습2
def mult(a, b):
    result = 1
    for i in range(a, b+1, 1):
        result *= i
    return result


print(mult(1, 3))
print(mult(2, 5))

# 실습3
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
print(possum, negsum)

mylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]
possum2, negsum2 = sum_pos_neg(mylist)
print(possum2, negsum2)

# 실습4
def vector_sum(vector, *vectors):
    res = list(vector)  # 무조건 주어짐

    for v in vectors:
        res[0] += v[0]
        res[1] += v[1]
    return res


v1 = [0, 1]
v2 = [0.5, 0.5]
v3 = [1, 0]
v4 = [6, 4]
v5 = [3.13, 2.72]

m1 = vector_sum(v1, v2, v3)
m2 = vector_sum(v1, v2, v3, v4)
m3 = vector_sum(v3, v5)

print(m1, m2, m3)

# 실습5
def merge_list(l1=[0], l2=[0]):
    result = []

    a = list(l1)
    b = list(l2)

    for i in a:
        result.append(i)

    for j in b:
        result.append(j)

    result = sorted(result)
    return result


l = [3, 5, 9, 1, 2]

ml1 = merge_list(l, [2, 1])
ml2 = merge_list([6, 9, 4])
ml3 = merge_list()

print(ml1)
print(ml2)
print(ml3)