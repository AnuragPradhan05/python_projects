questions = []
answers = []
correct_answer = []
amount=0

while(1):

    x=input("Enter a question you want to ask the player:\n")
    questions.append(x)
    y=input("Enter the correct answer:\n")
    answers.append(y)
    a=input("Enter the option:\n")
    b=input("Enter the option:\n")
    c=input("Enter the option:\n")
    d=input("Enter the option:\n")
    print("\n")
    print("The question is:\n",x)
    print("\n")
    print("The options are:\n")
    print(f"1. {a}\n2. {b}\n3. {c}\n4. {d}\n")

    Player = input("Write the answer of the given question:\n")

    correct_answer.append(Player)
    
    if(answers == correct_answer):
            amount+=2000
            print("You have won 2000 rs.\n")
    else:
            print("You have lost the match, sorry.\n")
            print("The total amount you have won is:\n",amount)
            break

print("Thank you for playing.\n")