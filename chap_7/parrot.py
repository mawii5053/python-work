# letting the user choose when to quit
prompt = "\ntell me something, and i will repeat it back to you: "
prompt += "\nenter 'quit' to end the program. "
message = ""
while message  != 'quit':
    message = input(prompt)
    print(message)

 