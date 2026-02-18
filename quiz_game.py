print("Welcome to the quiz program!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play : ")    
score = 0

answer = input("What does ASCII stand for ? ")
if answer.lower() == "american standard code for information interchange" :
    print("Correct !!")
    score += 1
else :
    print("You are wrong.")

answer = input("What does CPU stand for ? ")
if answer.lower() == "central processing unit" :
    print("Correct !! ")
    score += 1
else :
    print("You are wrong.")

answer = input("What does DVD stand for ? ")
if answer.lower() == "digital versatile disk" :
    print("Correct !! ")
    score += 1
else :
    print("You are wrong.")

answer = input("What does GUI stand for ? ")
if answer.lower() == "graphical user interface" :
    print("Correct !! ")
    score += 1
else :
    print("You are wrong.")

answer = input("What does GIGO stand for ? ")
if answer.lower() == "garbage in garbage out" :
    print("Correct !! ")
    score += 1
else :
    print("You are wrong.")

print(f"You got {score} questions correct!")
print(f"You got {(score/5)*100} %.")






 