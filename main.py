name = input("Enter name: ")
lower_name = name.lower()

if lower_name == 'james bond':
    print("We've been expecting you, Mr bond")
else:
    print("Access Denied: ", name)

# value = input("Enter an integer or float value: ")

# if value.isdigit():
#     print("Value is integer")
# elif value.isdecimal():
#     print("value is float")
# else:
#     print("is another else")


user_input = input("Enter an integer or float value: ")
print(type(user_input) )
print("is num ", user_input.isnumeric())
print("is dec ", user_input.isdecimal())
print("is alf ", user_input.isalpha())
print("is alf /num ", user_input.isalnum() )
'''
value = eval (user_input)
print (type(value))
if type(value) == int:
    print("Value is integer")
elif type(value) == float:
    print("Value es float")
else:
    print("IS another else")
'''
