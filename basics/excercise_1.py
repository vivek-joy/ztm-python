from datetime import date
birth_year = input('what your were born')
age = date.today().year - int(birth_year)

print(f'Your age is {age}')