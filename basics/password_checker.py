username = input("Enter your username ")
password  = input("Enter your password ")
password_length = len(password)
hidden_password = '*' * password_length
print(f'Your username is {username} and password is {hidden_password}, it is  {password_length} letters long')