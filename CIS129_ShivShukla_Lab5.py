#Shiv Shukla
# 2/26/25

"""This program is Lab 5: The Bottle Return Program. This program totals the numnber of bottles
collected in a week and yields the value alongside a total payout of 10 cents per bottle. The 
program can be looped for as many weeks as the user desires and will request a bottle count for 
each day of the week. Enjoy!"""

# Declare variables below
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = "y"

# Loop to run program again
while keep_going == "y":
    counter = 1
    total_bottles = 0
    while counter <= 7:
        today_bottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        total_bottles = total_bottles + today_bottles
        counter +=1
    total_payout = total_bottles * 0.1
    print()
    print(f"Total number of bottles collected is {total_bottles}")
    print(f"Total paid out is ${total_payout:,.2f}")
    print()
    keep_going = input("Do you want to enter another week's worth of data?\n(Enter y or n): ")
    print()