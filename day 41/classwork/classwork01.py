numbers = [1,2,3,4,5,6,7,8,9,10]
reversed_list = []
for i in range(len(numbers)):
    reversed_list.append(numbers[-i-1])
print(reversed_list)
