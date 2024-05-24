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
