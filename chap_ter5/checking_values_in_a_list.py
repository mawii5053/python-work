requested_foods = ['rice','beans','fish']
if 'moi' in requested_foods:
    print("requested_foods")
if "rice" in requested_foods:
    print(requested_foods)


print("\nchecking for value not in the list")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you can")

drug = "nurofen"
print("is drug == 'nurofen'? i predict true.")
print(drug == 'nurofen')

print("\nis drug == 'paracetamol' ? i predict false.")
print(drug == 'paracetamol')