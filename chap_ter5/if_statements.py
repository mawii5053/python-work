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



