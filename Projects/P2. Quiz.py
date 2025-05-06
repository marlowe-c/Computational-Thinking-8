NYC_points = 0
LA_points = 0

#Question 1
answer = input("Which do you prefer A) coffee, or B) matcha?")
if answer == "A":
    NYC_points += 1
elif answer == "B":
    LA_points += 1

#Question 2
answer = input ("Where would you prefer to live A) Beverly Hills, or B) The Hamptons?")
if answer == "A":
    LA_points += 1
elif answer == "B":
    NYC_points += 1

#Question 3
answer = input ("Which do you prefer A) tacos, or B) pizza?")
if answer == "A":
    LA_points += 1
elif answer == "B":
    NYC_points += 1

#Question 4
answer = input ("Which do you prefer A) The Knicks, or B) The Lakers?")
if answer == "A":
    NYC_points += 1
elif answer == "B":
    LA_points += 1

#Question 5
answer = input ("Which do you prefer A) seagulls, or B) pigeons?")
if answer == "A":
        LA_points += 1
elif answer == "B":
    NYC_points += 1

#End of Quiz:
if NYC_points > LA_points :
    print("You are a NYC person")
elif LA_points > LA_points :
    print("You are a LA person")