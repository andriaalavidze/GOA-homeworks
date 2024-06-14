more = []
less = []

for i in range(10):
    input_number = int(input("please enter number: "))
    if input_number == 100:
        continue
    elif input_number < 100:
        less.append(input_number)
    else:
        more.append(input_number)
print("this numbers are more than 100", more)
print("this numbers are less than 100", less)