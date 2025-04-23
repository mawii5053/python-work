prompt = "\nPlease enter the name of the pharmacy you have visited: "
prompt += "\n(Enter quit when you are finished.) "
while True:
    pharmacy = input(prompt)
if pharmacy == 'quit':
    break
else:
    print(f"I have to visit the facility of {pharmacy.title()} ")