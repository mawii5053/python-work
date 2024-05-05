bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

print(bicycles[0].title())

message = f"my first bicycle was a {bicycles[0].title()}"
print(message)


motocycles = ['honda','yamaha','suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)

motocycles.append('ducati')
print(motocycles)

motocycles = []
motocycles.append('yamaha')
motocycles.append('honda')
motocycles.append('suzuki')

print(motocycles)

motocycles.insert(0, 'ducati')
print(motocycles)

motocycles = ['bugatti', 'nissan', 'toyota']
print(motocycles)

del motocycles[0]
print(motocycles)
del motocycles[1]
print(motocycles)

motocycles = ['huggies','dettol', 'panadol']
print(motocycles)
popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)

food = ['beans', 'rice', 'fish']
last_ate = food.pop()
print(f"the last food i ate was a {last_ate.title()}.")

first_ate = food.pop(0)
print(f"the first food i ate was a {first_ate.title()}.")

food = ['beans', 'rice', 'fish']
print(food)
food.remove('beans')
print(food)

food =['beans','rice','garri']
print(food)
too_unhealthy = 'beans'
food.remove(too_unhealthy)
print(food)
print(f"\nA {too_unhealthy.title()} is too unhealthy for me to eat")

try_it_yourself = ['chapter_3 try_it_yourself']
print(try_it_yourself)

dinner_list = ['ogbu','paschal','lynda']
print(dinner_list)
dinner = dinner_list.pop(0)

print(f"\nI am inviting {dinner.title()} to a dinner")
dinner = dinner_list.pop()
print(f"\nI am inviting {dinner.title()} to a dinner")
dinner = dinner_list.pop()
print(f"\nI am inviting {dinner.title()} to a dinner")


