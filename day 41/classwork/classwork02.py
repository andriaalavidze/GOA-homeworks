numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
one_fifth = []
for i in range(len(numbers)):
    if numbers[i] % 5 == 0:
        one_fifth.append(numbers[i])
print(sum(one_fifth))
