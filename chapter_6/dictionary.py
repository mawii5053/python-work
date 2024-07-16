alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])
NEW_POINTS = alien_0['points']
print(f"you just earned {NEW_POINTS} points")

print("\n adding new key-value pairs")
emzor_0 = {'tablet': 'white','sachet' : 1}
print(emzor_0)
emzor_0['x_position'] = 0
emzor_0['y_position'] = 25
print(emzor_0)

print("\nstarting with an empty dictionary")
roziel_pharmacy = {}
roziel_pharmacy["ifeanyi"] = "director"
roziel_pharmacy["salary"] = 5000
print(roziel_pharmacy)

print("\nmodifying values in a dictionary")
roziel_pharmacy = {'color' : 'blue'}
print(f"the roziel is {roziel_pharmacy['color']}.")
roziel_pharmacy['color'] = 'red'
print(f"the roziel is now {roziel_pharmacy['color']}.")

roziel_pharmacy = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"original position: {roziel_pharmacy['x_position']}")
#move  the Pharmacist to the right
#determine how far to move the Pharmacist based on its current speed. 
if roziel_pharmacy['speed'] == 'slow':
    x_increment = 1
elif roziel_pharmacy['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast Pharmacist.
    x_increment = 3
#the new position is the old position plus the increment.
roziel_pharmacy['x_position'] = roziel_pharmacy['x_position'] + x_increment
print(f"new position: {roziel_pharmacy['x_position']}.")

print("\nRemoving K-value pairs")
roziel_pharmacy = {"dettol" : "brown" , "numbers" : 8}
print(roziel_pharmacy)
del roziel_pharmacy ["numbers"]
print(roziel_pharmacy)

print("\na dictionay of similar obejects")
favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil' : 'python',
    }
language = favorite_languages['sarah'].title()
print(f"sarah's favorite language is {language}.")

print("\n using get() to acess values")
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points','no point value assigned.')
print(point_value)