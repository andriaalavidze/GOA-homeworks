#   2) მომხმარებელს შეეკითხეთ სწავლობს თუარა გოაში, თუ სწავლობს
# შეეკითხეთ ომელ ჯგუფშია, თუ პასუხი იქნება ჯგუფი13 შეეკითეთ რომ 
# არის თუ არა გაბრიელი მისი მენტორი, თუ პასუხი იქნება კი უთხარით 
# რომ თქვენც აქ სწავლობთ და ნამდვილად გაბრიელია ორივეს მენტორი, 
# თუ პასუხი არიქნება გაბრიელი ყველა სხვა შემთხვევაში
# დაუბეჭდეთ რომ ის ტყუის და არარის სინამდვილეში ჯგუფ13-ში 

academy = input("are you learning in the Goa: ")
if academy == "yes":
    group = int(input("which group are you learning in: "))
    if group == 13:
        mentor = input("is your mentor Gabrieli: ")
        if mentor == "yes":
            print("i'm learning in the 13th group too and my mentor is Gabriel also")
        else:
            print("your lying your not in the 13th group")
    else:
        print("good i guess")
else:
    print("better join Goa and become chad")



