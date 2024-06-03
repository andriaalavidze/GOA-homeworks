#first .
def func(word_1, word_2, word_3, word_4):
    print(word_1 + " " + word_2 + " " + word_3 + " "  + word_4)
func(input("please enter word_1: "), input("please enter word_2: "), 
input("please enter word_3: "),  input("please enter word_4: "))

#second .
def question(question_1):
    if question_1 == "goa" or "Goa" or "GOA" or "Goa Oriented Academy"or "Goa oriented academy" or "goa oriented academy":
        print("your right")
    else:
        print("wrong answer, the best programing academy is Goa oriented academy")
question(input("which is the best programming academy: "))



