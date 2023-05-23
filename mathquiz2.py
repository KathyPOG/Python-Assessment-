#This is the second version of the math quiz

score = 0

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

if age <=(10):
    print("")
    print("You are not eligible for this quiz!")
    print("Have a good day!")

if age >=(19):
    print("")
    print("You are not eligible for this quiz!")
    print("Have a good day!")

if age in range(11,19):
          print("")
          print("You are eligible for this quiz!")
          print("")
          print("For each question, you will be given 4 choices, please choose from there!")
          print("When entering your answer, PLEASE ENTER FROM 1-4!")
          print("Best of luck!")
          print("")
          print("★---Level 1---★")
          print("")
          print("★---Question 1---★")
          print("")
          print("18+19")
          print("")
          print("1. 36")
          print("2. 37")
          print("3. 27")
          print("4. 41")
          print("")
          while True:
              try:
                  print("")
                  answer = int(input("Enter your answer here: "))
                  if answer == 2:
                      print("")
                      print("Correct!")
                      print("")
                      score+=1
                      break
                  else:
                      print("")
                      print("Incorrect! Try again!")
              except ValueError:
                  print("")
                  print("Please enter from 1-4!")
          print("★---Question 2---★")
          print("")
          print("19*3")
          print("")
          print("1. 57")
          print("2. 37")
          print("3. 6.33")
          print("4. 27")
          print("")
          while True:
              try:
                  print("")
                  answer = int(input("Enter your answer here: "))
                  if answer == 1:
                      print("")
                      print("Correct!")
                      score+=1
                      print("")
                      break
                  else:
                      print("")
                      print("Incorrect! Try again!")
              except ValueError:
                  print("")
                  print("Please enter from 1-4!")
          print("★---Question 3---★")
          print("")
          print("50/5")
          print("")
          print("1. 20")
          print("2. 5")
          print("3. 45")
          print("4. 10")
          print("")
          while True:
              try:
                  print("")
                  answer = int(input("Enter your answer here: "))
                  if answer == 4:
                      print("")
                      print("Correct!")
                      score+=1
                      print("")
                      break
                  else:
                      print("")
                      print("Incorrect! Try again!")
              except ValueError:
                  print("")
                  print("Please enter from 1-4!")
          print("★---Question 4---★")
          print("")
          print("29-12")
          print("")
          print("1. 16")
          print("2. 41")
          print("3. 17")
          print("4. 27")
          print("")
          while True:
              try:
                  print("")
                  answer = int(input("Enter your answer here: "))
                  if answer == 3:
                      print("")
                      print("Correct!")
                      score+=1
                      print("")
                      break
                  else:
                      print("")
                      print("Incorrect! Try again!")
              except ValueError:
                  print("")
                  print("Please enter from 1-4!")
          print("★---Question 5---★")
          print("")
          print("8²")
          print("")
          print("1. 55")
          print("2. 64")
          print("3. 46")
          print("4. 49")
          print("")
          while True:
              try:
                  print("")
                  answer = int(input("Enter your answer here: "))
                  if answer == 2:
                      print("")
                      print("Correct!")
                      score+=1
                      print("")
                      break
                  else:
                      print("")
                      print("Incorrect! Try again!")
              except ValueError:
                  print("")
                  print("Please enter from 1-4!")
          print("★---Question 6---★")
          print("")
          print("√49")
          print("")
          print("1. 9")
          print("2. 13")
          print("3. 7")
          print("4. 27")
          print("")
          while True:
              try:
                  print("")
                  answer = int(input("Enter your answer here: "))
                  if answer == 3:
                      print("")
                      print("Correct!")
                      score+=1
                      print("")
                      break
                  else:
                      print("")
                      print("Incorrect! Try again!")
              except ValueError:
                  print("")
                  print("Please enter from 1-4!")
          print("★---Question 7---★")
          print("")
          print("51*2+(4+8)")
          print("")
          print("1. 114")
          print("2. 112")
          print("3. 75")
          print("4. 118")
          print("")
          while True:
              try:
                  print("")
                  answer = int(input("Enter your answer here: "))
                  if answer == 1:
                      print("")
                      print("Correct!")
                      score+=1
                      print("")
                      break
                  else:
                      print("")
                      print("Incorrect! Try again!")
              except ValueError:
                  print("")
                  print("Please enter from 1-4!")
                

print("★------------------------------------------------------------★")
print("")
print("Congratulation", name,"! You have completed this quiz!")
print("Your score is" ,score,"!")
print("")
print("★------------------------------------------------------------★")
