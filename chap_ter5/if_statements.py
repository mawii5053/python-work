cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
else:
    print(car.title())

    print("\nchecking for equality")

car = 'audi'
if car == 'audi':
    print(car)


car = 'audi'
if car == 'bmw':
    print(car)

car = 'Audi'
if car == 'audi':
    print(car)

drugs = 'Morphine'
if drugs.lower() == 'morphine':
    print(drugs)

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("have you registered to vote yet!")

print("\nif-else statement")
age = 17
if age >= 18 :
    print("you are old enough to vote")
    print("HAVE YOU REGISTERED TO VOTE!")
else:
    print("sorry ,you are too young to vote")
    print("please register to vote as soon as you turn 18.")

print("\nthe if-elif-else chain")
age = 12
if age < 4:
    print("admission cost is $0. ")
elif age < 18:
    print("your admission cost is $25. ")
else:
    print("your admission cost is $40. ")

print("\nOR.")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"your admission cost is ${price}. ")

print("\nusing multiple elif blocks.")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20   
print(f"your admission cost is ${price}. ")    

print("\nomitting the else block.")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 60:
    price = 40
elif age >= 65:
    price = 20
print(f"your admission cost is ${price}. ")    

print("\nTesting multiple condition.")
requested_toppings = ["mushrooms", "extra cheese"]
if 'mushrooms' in requested_toppings:
    print("adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")
print("\nfinished making your pizza!")

alien_colour = ['green', 'yellow', 'red']
if 'green' in alien_colour:
    print("player should earn 5 points.")
if 'pink' in alien_colour:
    print("the player should pay $10.")    


alien_colour = ['green', 'yellow', 'red', 'gold', 'purple']
alien_colour = 'green'
if "green" == alien_colour:
    print("player just earned 5 points for shooting an alien.")    
if "black" in alien_colour:  
    print("player just earned 10 points")  

alien_colour = ['green', 'yellow', 'red', 'gold', 'purple']
if "yellow" in alien_colour:
    print("you are good to go")
else:
    print("stay back and wait for the next batch")  

alien_colour = ['green', 'yellow', 'red', 'gold', 'purple']  
if "green" in alien_colour:
    points = 5
elif "yellow" in alien_colour:
    points = 10
elif "red" in alien_colour:
    points = 15
else:
    points = 20
print(f"these are the various {points}")

age = 2
if age < 2:
    print("you are a baby.")

print(f"\nUsing if statement for list and checking for special item")

pharmaceutical_products = ['cosmetics', 'medicine', 'anticeptics']
for pharmaceutical_product in pharmaceutical_products:
    print(f"adding {pharmaceutical_product}. ")
print("\nfinished building your factory")  

pharmaceutical_products = ['cosmetics', 'medicine', 'anticeptics']
for pharmaceutical_product in pharmaceutical_products:
    if pharmaceutical_product == 'medicine':
        print("sorry, we are out of medicine it right now.")
else:
    print(f"adding {pharmaceutical_product}.")
print("\nfinished building your factory")  

print("\nCHECKING THAT A LIST IS NOT EMPTY.")
pharmaceutical_products = []
if pharmaceutical_products:
    for pharmaceutical_product in pharmaceutical_products:
        print(f"adding {pharmaceutical_product}.")
    print("\nfinished making your pizza!")
else:
    print("are you sure you want drugs")      

print("\nUsing multiple list")

available_toppings = ["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings = ["mushrooms","french fries","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}.")
else:
    print(f"sorry, we don't have {requested_topping}")
print("\nfinished making your pizza!")    

print("\ntry it yourself")
usernames = ['kafayat','victoria','martha','rosemary','admin']
for username in usernames:
    print(f"you are welcome {username}")
if username == 'admin':
    print(f"hello admin, would you like to see a status report ?")
else:
    print(f"hello {username} , thank you for logging in again")    

 
usernames = []
if not usernames:
    print(f"we need to find some users")

current_users = ['biodun','ayo','bidemi','sikirat','dapo']
new_users = ['chidi','nkem','ayo','bidemi','dozie'] 
for new in new_users:
    if new in current_users:
        print(f"please enter a new name ")  
    if new not in current_users:
        print(f"user name available") 
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")                   





      



    

