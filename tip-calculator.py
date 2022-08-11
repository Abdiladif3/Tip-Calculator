print("Welcome to the tip calculator! ")

# get calculations from user
total = float(input("What was the total bill? $"))

tip = float(input('How much tip would you like to give? 10, 12, or 15? '))

split = int(input('How many people to split the bill? '))

# split total bill between amount of people
newsplit = (total / split)

# update tip % by adding 1 at the end which is (total + tip)
newtip = ((tip / 100) + 1)

# multiply newsplit & newtip, and lastly round to 2 dp
newtotal = round((newsplit * newtip), 2)

# print final output
print(f"Each person should pay: ${newtotal}")
