drink_list = ["cola", "fanta", "sprite", "water", "fuse_tea", "prime"]
print("countdown starts from 0")
users_choice = int(input("please enter witch drink you want:"))
if users_choice >=0 and users_choice <=5:
    print("your drink is:" + " " + str(drink_list[users_choice]))
else:
    print("this number is invalid please try again")