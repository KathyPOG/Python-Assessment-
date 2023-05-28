#This is the 4th version of the math quiz

import time #This import time imports the keyword to make the code available or else the code won't worlk
def time_convert(sec): #Function to calculate the time taken to complete the code
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time taken to complete the quiz = {0}:{1}:{2}".format(int(hours),int(mins),sec))

score = 0  #setting up variables
point = 0
trial_lvl = 1
trial_num = 0
level = 1
opt_num = 0

qa = {'99-124':1,'185/5':4,'√81*8':3} #Dictionary to store the questions and answers

op=[['1. -25   2. -26   3. -31   4. -22'], #List to store all the answer choices
    ['1. 38   2. 41   3. 40   4. 37'],
    ['1. 64   2. 40   3. 72   4. 81']]

qa1 = {'18+19':2, '19*3':1,'50/5':4,'29-12':3,'8²':2,'√49':3,'51*2+(4+8)':1} 

op1=[['1. 36   2. 37   3. 27   4. 41'],
         ['1. 57   2. 37   3. 6   4. 27'],
         ['1. 20    2. 5   3. 45   4. 10'],
         ['1. 16   2. 41   3. 17   4. 27'],
         ['1. 55   2. 64   3. 46   4. 49'],
         ['1. 9   2. 13   3. 7   4. 27'],
         ['1. 114   2. 112   3. 75   4. 118']]

qa2 = {'410*52':3, '23*18-10*10':3,'598*4/2':3,'2898-561':1,'52.9²':4,'√859':1,'289*2.9-(22-12.1)':2}

op2=[['1. 21223   2. 21037   3. 21320   4. 21220'],
         ['1. 324   2. 327   3. 314   4. 312'],
         ['1. 1691    2. 1196   3. 1169   4. 1961'],
         ['1. 2337   2. 2372   3. 2272   4. 2232'],
         ['1. 2788.2   2. 2688.54   3. 2799.4   4. 2798.41'],
         ['1. 29.31   2. 27.9   3. 31.45   4. 27.99'],
         ['1. 830.2   2. 828.2   3. 820.1   4. 822.8']]

qa3 = {'42*6-1':4, '√456-41':2,'√486/6':1,'(134-13)*2':3,'99²/9':4,'√100*12':4,'109*12-(12+69)':3}

op3=[['1. 257   2. 261   3. 252   4. 251'],
         ['1. 19.65   2. -19.65   3. -21.34   4. 34.5'],
         ['1. 9   2. 8   3. 9.9   4. 8.9'],
         ['1. 243   2. 241   3. 242   4. 244'],
         ['1. 991   2. 990   3. 1099   4. 1089'],
         ['1. 121   2. 201   3. 121   4. 120'],
         ['1. 1727   2. 1227   3. 1721   4. 1223']]
         
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
        print("Age should be entered in a positive integer eg. 9")


if age <=(10):
    print("")
    print("You are not eligible for the quiz")
    print("Have a good day.")
    exit()

if age >=(19):
    print("")
    print("You are not eligible for the quiz")
    print("Have a good day.")
    exit()

if age in range(11,19):
    print("")
    print("You are eligible for this quiz!")
    print("")
    print("★--------------------★")
    print("")
    print("We will determine which level you are suitable for by asking you three questions")
    print("When entering your answer, PLEASE ENTER FROM 1-4!")
    print("Best of luck!")
    print("")
    print("★---Practice Trial---★")
    for k,v in qa.items():
        print("")
        print("★--- Question",trial_lvl,"---★")
        print("")
        print(k)
        print("")
        for option in op[trial_num]:
            print(option)
            print("")
            trial_num+=1
            trial_lvl+=1
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
                        print("")
                        point+=1
                        break #This breaks the loop so the user can carry onto the next question
                    else:
                        print("")
                        print("Incorrect!")
                        print("You got this!")
                        print("")
                        break
                except ValueError: #This is used to trap errors and notify the user about it
                    print("")
                    print("Please enter from 1-4!")

    if point==3:
        print("You are suitable for level 3!")
        print("For each question, you will be given 4 choices, please choose from there!")
        print("When entering your answer, PLEASE ENTER FROM 1-4!")
        print("Best of luck!")
        start_time = time.time()
        for k,v in qa3.items():
            print("")
            print("★--- Question",level,"---★")
            print("")
            print(k)
            print("")
            for option in op3[opt_num]:
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
                            break
                        else:
                            print("")
                            print("Incorrect!")
                            print("You got this!")
                            break
                    except ValueError:
                        print("")
                        print("Please enter from 1-4!")

    if point in range(0,1):
        print("You are suitable for level 1!")
        print("For each question, you will be given 4 choices, please choose from there!")
        print("When entering your answer, PLEASE ENTER FROM 1-4!")
        print("Best of luck!")
        start_time = time.time() #This starts the stopwatch/timer
        for k,v in qa1.items():
            print("")
            print("★--- Question",level,"---★")
            print("")
            print(k)
            print("")
            for option in op1[opt_num]:
                print(option)
                print("")
                opt_num+=1
                level+=1
                while True:
                    try:
                        print("")
                        answer = int(input("Enter your answer here: "))
                        if answer<1 or answer>4: #This is used so the user will only type between 1-4 as thats the only choices
                            raise ValueError
                        if answer == v:
                            print("")
                            print("Correct!")
                            print("Impressive!")
                            score+=1
                            break
                        else:
                            print("")
                            print("Incorrect!")
                            print("You got this!")
                            break
                    except ValueError:
                        print("")
                        print("Please enter from 1-4!")
    if point==2:
        print("You are suitable for level 2!")
        print("For each question, you will be given 4 choices, please choose from there!")
        print("When entering your answer, PLEASE ENTER FROM 1-4!")
        print("Best of luck!")
        start_time = time.time()
        for k,v in qa2.items():
            print("")
            print("★--- Question",level,"---★")
            print("")
            print(k)
            print("")
            for option in op2[opt_num]:
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
                            break
                        else:
                            print("")
                            print("Incorrect!")
                            print("You got this!")
                            break
                    except ValueError:
                        print("")
                        print("Please enter from 1-4!")

if score==7:
    print("")
    print("You have gotten every question correct!")
    print("This will be the last question and if you answer correctly, you will be awared 3 points!")
    print("Best of luck!")
    print("")
    print("★--- Final Question ---★")
    print("")
    print("You have x amount of candy and I have x amount of candy.")
    print("The total amount of candy we both have is 96.")
    print("However I have 12 times the amount you have.")
    print("How much do you have?")
    while True:
            try:
                print("")
                answer = int(input("Enter your answer here: "))
                if answer == 8:
                    print("")
                    print("Correct!")
                    print("Impressive!")
                    score+=3
                    break 
                else:
                    print("")
                    print("Incorrect!")
                    print("You got this!")
                    break
            except ValueError: 
                print("")
                print("Please enter in integer form (eg. 9)")

    print("")
    print("★------------------------------------------------------------★")
    print("")
    print("Congratulation", name,"! You have completed this quiz!")
    print("Your score is" ,score,"!")
    end_time = time.time() #This stops the stopwatch/timer
    time_lapsed = end_time - start_time #This is calculating the time taken
    time_convert(time_lapsed)
    print("")
    print("★------------------------------------------------------------★")

else:
    print("")
    print("★------------------------------------------------------------★")
    print("")
    print("Congratulation", name,"! You have completed this quiz!")
    print("Your score is" ,score,"!")
    end_time = time.time() #This stops the stopwatch/timer
    time_lapsed = end_time - start_time #This is calculating the time taken
    time_convert(time_lapsed)
    print("")
    print("★------------------------------------------------------------★")

