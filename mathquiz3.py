#This is the third version of the math quiz

qa = {'18+19':2, '19*3':1,'50/5':4,'29-12':3,'8²':2,'√49':3,'51*2+(4+8)':1}

options=[['1. 36   2. 37   3. 27   4. 41'],
         ['1. 57   2. 37   3. 6   4. 27'],
         ['1. 20    2. 5   3. 45   4. 10'],
         ['1. 16   2. 41   3. 17   4. 27'],
         ['1. 55   2. 64   3. 46   4. 49'],
         ['1. 9   2. 13   3. 7   4. 27'],
         ['1. 114   2. 112   3. 75   4. 118']]

score = 0
level = 1
opt_num = 0
         
print("")
print("---Welcome to the Math Quiz---")
print("")
print("To ensure your safety, we will ask some questions.")
print("")
print("The age limit for this quiz is 11-18")
print("")
name = input("Enter your name here: ")

while True:
    try:
        print("")
        age = int(input("Enter your age here: "))
        break

    except ValueError:
        print("")
        print("Age should be entered in integer eg. 9")

if age in range(11,19):
    print("")
    print("You are eligible for this quiz!")
    print("")
    print("For each question, you will be given 4 choices, please choose from there!")
    print("When entering your answer, PLEASE ENTER FROM 1-4!")
    print("Best of luck!")
    print("")
else:
    print("")
    print("You are not eligible for this quiz!")
    print("Have a good day!")

for k,v in qa.items():
    print("")
    print("★--- Question",level,"---★")
    print("")
    print(k)
    print("")
    for option in options[opt_num]:
        print(option)
        print("")
        opt_num+=1
        level+=1
        while True:
            try:
                print("")
                answer = int(input("Enter your answer here: "))
                if answer<1 or answer>4:
                    raise ValueError
                if answer == v:
                    print("")
                    print("Correct!")
                    print("Impressive!")
                    score+=1
                    print("")
                    break
                else:
                    print("")
                    print("Incorrect!")
                    print("You got this!")
                    print("")
                    break
            except ValueError:
                print("")
                print("Please enter from 1-4!")


print("★------------------------------------------------------------★")
print("")
print("Congratulation", name,"! You have completed this quiz!")
print("Your score is" ,score,"!")
print("")
print("★------------------------------------------------------------★")


            
                          
                  

