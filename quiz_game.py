print("WELCOME TO MY COMPUTER QUIZ!")
# Ask the users if they want ot play my game

#created a variable named "playing","name" and asked user with help of "input" function which allows users to type in the console when the program runs and also  This function first takes the input from the user and converts it into a string, inside of input we put "prompt"
name = input("Enter Your Name : ")
print("Your Name is : ", name)

playing = input("Do You Want To Play ? ") # here we added space because user will start one space after question mark  

# now we want to check the persons ans regardless of something i.e capital y,e,s,n,o whatever he or she types it should consider same 

# we want to check if the user typed yes or not and if not we will end the program 
# for that we will use lower() function which will lower the string whatever the person types


# for that we will use if statement 
# which will allow conditionally to compare the value 

if playing.lower() != "yes":
    quit() # Exit Programs With the quit() Function in Python

print("Okay! Let's play: ) " , name) 

# SCORE
score = 0 


# question 1
# asking users the questions
answer1 = input("What does CPU Stands for ? ")
# for checking typing the actual answer 
if answer1.lower() == "central processing unit":
    print("Correct! ")
    score += 5
# if users get this wrong then we will tell them this answer is incorrect 
else:
    print("Incorrect :(")


# question 2
answer1 = input("What does GPU Stands for ? ")
if answer1.lower() == "graphics processing unit":
    print("Correct! ")
    score += 5
else:
    print("Incorrect :(")

# question 3
answer1 = input("What does RAM Stands for ? ")
if answer1.lower() == "random access memory":
    print("Correct! ")
    score += 5
else:
    print("Incorrect :(")

# question 4
answer1 = input("What does PSU Stands for ? ")
if answer1.lower() == "power supply":
    print("Correct! ")
    score += 5
else:
    print("Incorrect :(")

# question 5
answer1 = input("IC chips used in computers are usually made of ")
if answer1.lower() == "silicon":
    print("Correct! ")
    score += 5
else:
    print("Incorrect :(")

print("Your Final Score " +  str(score)  + " Questions Correct")

# GIVNING PRECENTAGE 
print("Your Final Percentage " +  str((score/5) * 100)  + "%.")