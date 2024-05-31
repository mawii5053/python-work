players = ['dozie','rose','ugonna','sheila','nancy']
print(players[0:3])
print(players[1:4])
print(players[ :4])
print(players[2: ])
print(players[-3:])

print('looping through a SLICE')


players = ['dozie','rose','ugonna','sheila','nancy']
print("here are the first three players on my team")
for player in players[:3]:
    print(player.title())

print('\ncopying a list')    

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("my favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are :")
print(my_foods)
print("\nmy friend's favorite food are:")
print(friend_foods)

print('\nwhen aslice is not added when copying a list')

my_foods = ['pizza','falafel','carrot cake']

# this doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are :")
print(my_foods)
print("\nmy friend's favorite food are:")
print(friend_foods)

print('\ntry it yourself on slice')

anticeptics = ['dettol','savlon','izal','purit','huggies','kiss','anorol']
print("the first three items in the list are:")
print(anticeptics[0:3])
print("\nthree items from the middle of the list are:")
print(anticeptics[2:5])
print("\nThe last three items in the list are:")
print(anticeptics[4:])

print('\nfuther more')
my_menu = ['fufu','garri','yam','rice',]
azaya_menu = my_menu[:]
my_menu.append('egg')
azaya_menu.append('pupu')
print(my_menu)
print(azaya_menu)
print("\nmy favorite menu is")
for menu in my_menu[:5]:
    print(menu.title())
for menu in azaya_menu[:5]:
    print(menu.title())

print('\nTUPLES')
print('for example')

dimension = (200, 50)
print(dimension[0])
print(dimension[1])
print('\nlooping through all values in a tuple')
print('for example')
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

print('\nwriting over a tuple')
print('for example')
dimensions = (200, 50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nmodified dimensions:")
for dimension in dimensions:
    print(dimension)

print("\ntry it yourself")
buffets = ('rice', 'bread', 'egg', 'fruit', 'cheese')
for buffet in buffets:
    print(buffet)

buffets = ('rice', 'bread', 'cakes', 'salads', 'pies')
print("\nmodified buffets:")
for buffet in buffets:
    print(buffet)
    

