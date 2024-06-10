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
if "green" in alien_colour:
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
