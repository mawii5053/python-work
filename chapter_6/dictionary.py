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

print('\n')

girl = {'first_name':'victoria', 'last_name': 'ekine', 'age': '17', 'city': 'port harcourt'}

print(girl['first_name'])

print(girl['last_name'])

print(girl['age'])

print(girl['city'])


print('\n')

roziel_pharmacy = {

    'martha': 79, 

    'silver': 63, 

    'victoria': 17, 

    'mawii': 50, 

    'rose': 29

    }

for key, value in roziel_pharmacy.items():

    print(f"{key} favorite number is {value}")

roziel_pharmacy = {'username': 'nnadozie',
'first' : 'ifeanyi',

'last' : 'agwulonu',

}

for key, value in roziel_pharmacy.items():

    print(f"\nkey:{key}")

    print(f"value:{value}")


print(f"\nexample 2")

favorite_languages ={

    'jen': 'python',

    'sarah': 'C', 

    'edward': 'ruby', 
    'phil' : 'python',

    }

for name, language in favorite_languages.items():

    print(f"{name.title()}'s favorite language is {language.title()}.")


print(f"\n*looping through all the key in a dictionary*")

favorite_languages ={

    'jen': 'python',

    'sarah': 'C', 

    'edward': 'ruby', 
    'phil' : 'python',

    }

for name in favorite_languages.keys():

    print(name.title())


print("\n*another example*")


favorite_languages = {

    'jen': 'python',

    'sarah': 'C', 

    'edward': 'ruby', 
    'phil' : 'python',

    }

friends = ['jen','sarah']

for name in favorite_languages.keys():

    print(name.title())

for name in friends:

    language = favorite_languages[name].title()
    #print(     



cephalosporin = {'colour' : 'green' , 'points' : 50}