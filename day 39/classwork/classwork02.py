number = []
input = int(input("please enter number: "))
for i in range(1):
    number.append(i)
even = []
odd = []
for i in number:
    if i %2  == 0:
        even.append(i)
for i in number:
    if i %2  >0:
        odd.append(i)
print("even", even)
print("odd", odd)