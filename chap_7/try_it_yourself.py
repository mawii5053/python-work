message = input("what kind of car woould you like?  ")
print(f"\nlet me see if i can get you {message} 2028 model ")
dining_group = input("how many people are in the dining group?  ")
dining_group = int(dining_group)
if dining_group >= 8:
    print(f"\nthey'll have to wait for a table")
else:
    print(f"\ntheir table is ready")

number = input("enter a number, and i'll tell you if its a multiple of 10.  ")
number = int(number)
if number % 10 == 0:
    print(f"\nthe number {number} is a multiple of 10. ")
else:
    print(f"\nthe number {number} is not a multiple of 10")