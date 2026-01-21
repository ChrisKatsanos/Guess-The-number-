import random
guess = 105
number = random.randint(1,100)
count = 0
win = 0
lives = 5
while guess  !=  number and lives > 0:
     guess = int(input("Guess a number between 1 and 100:"))
     count += 1
     if guess == number :
         print("you won!")
         win = 1
         break
     elif guess < number:
         print("up")
         lives -= 1
     elif guess > number:
         print("down")
         lives -=1

     print ("you have", lives, "lives left")


if win == 1:
    print ("won after " + str(count) + " guesses")
else :
    print ("lost after all your lives")








