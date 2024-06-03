def function(list):
    sum = 0
    for i in range(0,len(list)):
        if i % 2 == 0:
            sum += list[i]
    return sum

print(function([1,2,3,4,5]))
            

        