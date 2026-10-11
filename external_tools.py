import random, datetime, os 

from math import sqrt, pi 


number = random.randint(1, 100)
choice = random.choice(["rock", "paper", "scissors"])
print(number)
print(choice) 
now = datetime.datetime.now()
print(now)

current_directory = os.getcwd()
print(current_directory)

