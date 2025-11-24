def showGreeting(userName):
    msg = f"hello ,{userName}, Bienvenida"
    return msg
#main
print("Enter your name: ")
user_name = input()
message =showGreeting(user_name)
print(message)


