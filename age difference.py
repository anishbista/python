import random
import datetime
now = datetime.datetime.now()
random_sentences = ["dont talk about future you may die in 2020 ",
                    "are you from future", 
                    "are you mad", 
                    "this is bullshit man fuck off"]
year = input("Enter your birth year in AD \n")
year = int(year)
if(year > now.year):
    randInt = random.randint(0, 3)
    print(random_sentences[randInt])
else:
    age = now.year - year
    print("Your age is " + str(age) + "year old")

