correct_password = "nimesh"
name = input("Enter your name: ")
sur_name = input("Enter your surname: ")
user_password = input("Enter the password:")

while (correct_password != user_password):
    user_password = input("Wrong password! Please enter the password again: ")

message = "Hi %s %s, you are logged in" % (name, sur_name)
print(message)
