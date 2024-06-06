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