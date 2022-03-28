#Oregon Trail Game

#imports
from glob import glob
import random

#begining story
print()
print()
print("__________________________________________________STORY____________________________________________________________________")
print(" You are a farmer who wants to go start a new life. You go from Independance, MO and are making the dangerous journey.")
print(" To Oregon using the Oregon Trail. You may come across danger but it could be sunshines and rainbows.")
print(" You need to get there before the insane winter starts which is 12/31 Well lets get this 2000 miles journey started!")
print()



#variables
player_health = 5

#how much foods they have
pounds_of_food = 500

#miles to go
miles_left_in_the_trip = 2000

#current month in the game
current_month = 3

#current day in the game
current_day = 1

#months of the year
MONTHS = [
    "dummy","January","Febuary","March", "April" , "May", "June", "July",
     "August", "September", "October", "November", "December"
    ]

#tells me what the months with 30 days are
MONTHS_WITH_30_DAYS = ["April", "June", "September", "November"]


#FUNCTIONS

#ask the program for help
def help():
    print()
    print ("The following commands that you can do are travel, rest, hunt, status, help, and quit.")
    print ("Travel is to go further into your adventure")
    print ("Hunt to get more food, but you might get hurt.")
    print ("Status to see your health and how much further in your journey")
    print ("help well this...")
    print ("Quit to stop the game.")

#gives the player info
def status():
    print(f"It is {MONTHS[current_month]} {current_day}")
    print(f"You currently have {str(player_health)} health remaning.")
    print (f" You have {pounds_of_food} left.")
    print (f" You have {miles_left_in_the_trip} miles to go!")

#player gets hurt
def hurt():
    global player_health
    player_health -= 1

#player eats food
def eat_food():
    global pounds_of_food
    pounds_of_food -= 5

#travels the player miles
def travel():
    global miles_left_in_the_trip
    consume_food(days)
    days = random.randint(3, 7)
    miles_traveled = random.randint(30, 60)
    miles_left_in_the_trip -= miles_traveled
    print (f"You took {days} days to travel {miles_traveled} miles.")
    print(f" You have {miles_left_in_the_trip} miles left in your trip to Oregon.")
    add_day(days)


#player hunts for more food
def hunt():
    global pounds_of_food
    pounds_of_food += 100
    print ("You succesfully got 100 more pounds of food! NICE JOB!")
    will_you_get_hurt = random.randint (1,3)
    if will_you_get_hurt == 3:
        hurt()
        print("While hunting a pack of wolves decided to attack you. You lost some health.")

#adds days program
def add_day(days):
    global current_day
    global current_month
    current_day += days
#roll over to the new month for 30 days
    if MONTHS[current_month] in MONTHS_WITH_30_DAYS:
        if current_day > 30:
            current_day -= 30
            current_month += 1
#months with 31 days
    else:
        if current_day > 31:
            current_day -= 31
            current_month += 1


#player rests
def rest():
    global player_health
    if player_health < 5:
        days = random.randint(2, 5)
        add_day(days)
        consume_food(days)
        player_health += 1
        print (f"You rested and gained 1 health in the span of {days} days.")
    elif player_health == 5:
        days = random.randint(2, 5)
        add_day(days)
        consume_food(days)
        print (f"You wasted days and food because your already at the 5 maximum health dummy.")


def consume_food(days):
    global pounds_of_food

    food_consumed_this_turn = 5 * days

    






game_over = True
#game loop 
while game_over is True:
    print()
    print("------------New Day------------")
    print()
        #print the day
    print(
        f"It is {MONTHS[current_month]} {current_day}"
        )


    #player eats 5lbs. of food
    eat_food()



    #player chooses what they want to do.
    players_choice = input("What would you like to do? [travel, rest, hunt, status, help, or quit.] ")
    if players_choice == "travel":
        travel()
    elif players_choice == "status":
        status()
    elif players_choice == "help":
        help()
    elif players_choice == "hunt":
        hunt()
    elif players_choice == "rest":
        rest()
    elif players_choice == "quit":
        print("Goodbye!")
        game_over = False
        
    if miles_left_in_the_trip <= 0:
        print("Congrats! You made it to Oregon in just in time!")
        game_over = False

    if MONTHS[current_month] == 12 and current_day == 31:
        print("You didnt make it in time. Your wagon is blown out of control and you loose all your things. You die in the cold.")
        game_over = False
