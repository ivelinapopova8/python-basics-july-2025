username = input()
password = input()
new_password = input()

while True:
    if new_password == password:
        print(f"Welcome {username}!")
        break
    else:
        new_password = input()
