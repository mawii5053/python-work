# how the input() function works
message = input("tell me something , and i will repeat it back to you:  ")
print(message)

# each time you use the input() function , you should include a clear, easy-to-follow prompt that tells the user exactly what kind
# of information you are looking for.
name = input("please enter your name:  ")
print(f"\nhello, {name} ")

# writing clear prompt that is more than one line
prompt = "if you tell us who you are, we can personalize the message you see. "
prompt += "\nwhat is your first name ?  "
name = input(prompt)
print(f"\nhello, {name} ")

# USING INT() TO ACCEPT NUMERICAL INPUT
age = input("how old are you?  ")
print(age)
age = input("number of plates in my house? ")
age = int(age)
age >= 18
