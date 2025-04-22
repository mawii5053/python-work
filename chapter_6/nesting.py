roziel_0 = {'camosunate': 'orange', 'age' : 1}
roziel_1 = {'camosunate' : 'pink', 'age' : 6}
roziel_2 = {'camosunate' : 'blue', 'age' : 13}
roziels = [roziel_0, roziel_1, roziel_2]
for roziel in roziels:
    print(roziel)

#make an empty list for storing roziels
# roziels = []
# make 30 green roziels
for roziel_number in range (30):
    new_roziel = {'camosunate':'red', 'age': 20, 'speed': 'fast'}
    roziels.append(new_roziel)
#show the first 5 roziels.
for roziel in roziels[:5]:
    print(roziel)        
    print('...')
#show how many roziels have been created.
print(f"total number of roziels: {len(roziels)}")


#store information about a pizza being ordered.
pizza = {
'crust' : 'thick',
'toppings' : ['mushrooms', 'extra cheese'],
}
#summarize the order
print(f"you ordered a {pizza['crust']}-crust pizza" 
    " with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

#you can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary
favorite_languages = {
'jen' : ['python', 'ruby'],
'sarah' : ['c'],
'edward' : ['ruby', 'go'],
'phil' : ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are :")
    for language in languages:
        print(f"\t{language.title()}")

#a DICTIONARY IN A DICTIONARY
user = {
'roziel' : {
'first' : 'peace',
'last' : 'alfred',
'location' : 'egbelu',
},
'silma' : {
'first' : 'martha',
'last' : 'achese',
'location' : 'ogun',
},
}
for username, user_info in user.items():
    print(f"\nusername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tfull name : {full_name.title()}")
    print(f"\tLocation : {location.title()}")
    print(exit)