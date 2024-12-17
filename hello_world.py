# variable.
print("hello python world")
message = "hello python world"
print(message)

message = "hello python crash course world"
print(message)

message = "i love food"
print(message)

message = "sex is sweet"
print(message)

name = "ada love"
print(name.title())

name = "ada love"
print(name.upper())
print(name.lower())

first_name = "nnadozie"
last_name = "agwulonu"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "nnadozie"
last_name = "agwulonu"
full_name = f"{first_name} {last_name}"
print(f"hello, {full_name.title()}")

first_name = "ifeanyi"
last_name = "nnadozie"
full_name = f"{first_name} {last_name}"
message = f"hello, {full_name.title()}"
print(message)

print("python")
print("\tpython")

print("languages:\npython\nc\njavascript")

print("languages:\n\tpython\n\tc\n\tjavascript")

favorite_language = 'python   '
print(favorite_language)

favorite_language = 'python'
favorite_language = favorite_language.rstrip()
print(favorite_language)

# string
favorite_language = "   python   "
favorite_language = favorite_language.rstrip()
favorite_language = favorite_language.lstrip()
favorite_language = favorite_language.strip()
print(favorite_language)

message = "one of python's strenght is its diverse community."
print(message)

def rectangle_area(length=2,width=3):
    """return a rectangle's area"""
    return length * width
print(rectangle_area)