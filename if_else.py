import random

club = ("Real Madrid", "Liverpool" , "Man utd" , "Barcelona", "Bayern" , "Mancity", "Arsenal")

football_club = input("Enter your club name: ")

if football_club in club:
    print("You are a bigger club")
else:
    print("You are a smaller club")
    