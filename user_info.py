def get_user_info(*args, **kwargs):
    user_info = {}

    if len(args) >= 3:
        user_info['name'] = args[0]
        user_info['email'] = args[1]
        user_info['age'] = args[2]
    else:
        user_info['name'] = kwargs.get('name', input("Enter your name: "))
        user_info['email'] = kwargs.get('email', input("Enter your email: "))
        user_info['age'] = kwargs.get('age', input("Enter your age: "))

    return user_info

user_data = get_user_info(name=(input("Enter your name:")), age=(input("Enter your age:")))
print("User Information:")
# print("Name:", user_data['name'])
print("Email:", user_data['email'])
# print("Age:", user_data['age'])
