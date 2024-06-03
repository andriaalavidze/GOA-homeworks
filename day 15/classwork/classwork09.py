def  min_and_max(a):
    min = a[0]
    max = a[0]

    for i in a:
        if min > i:
            min = i
        elif max < i:
            max = i

    print("min is:" + str(min))
    print("max is:" + str(max))

min_and_max([2,3,6,1,9,1])