import random
n = random.randint(1,20)
chance = 4
tries = 1
word = "first"
keep_playing = True
while keep_playing == True :
    if tries == 1 :
        number = int(input("Enter " + word +  " number between 1 to 20 : "))
    if tries == 2 :
        word = "second"
        number = int(input("Enter " + word +  " number between 1 to 20 : "))
    if tries == 3 :
        word = "third"
        number = int(input("Enter " + word +  " number between 1 to 20 : "))
    if tries == 4 :
        word = "fourth"
        number = int(input("Enter " + word +  " number between 1 to 20 : "))        
    chance = chance - 1
    tries = tries + 1
    if (number > 20 or number < 1) : 
        print ("Look at top it says from 1 to 20")
    elif number == n:
        print("Wait a minute that is a good guess, Congrats ! ")
        keep_playing = False
    elif number == n+2 :
        print("Sorry your guess is close but more than actual number")
    elif number == n-2 :
        print("Sorry your guess is close but more than actual number")
    elif number > n :
        print("Sorry your guess is more than actual answer")
    elif number < n :
        print("Sorry your guess is less than actual number") 
    elif number != n:
        print("What a waste that is absolutely wrong guess, TRY AGAIN!")
    if chance == 0 :
        print("That is all chance you got in your life, Iam kidding try next time and \n if you wanna know correct it is " + str(n))
        keep_playing = False   
        
        



   
