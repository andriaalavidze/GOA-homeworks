def func(list):
    sum_1 = 0
    sum_2 = 0
    list_1 = []
    for i in list:
        if i % 2 == 0:
            sum_1 += i
        else:
            sum_2 += i
    list_1.append(sum_1)
    list_1.append(sum_2)
    return list_1
print(func([1,2,3,4,5]))
