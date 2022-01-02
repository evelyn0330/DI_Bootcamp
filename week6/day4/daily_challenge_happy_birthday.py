birh_date = input("Please, give me your birthdate in this format DD/MM/YYYY: ")
day, month, year = birh_date.split('/')
current_date = [11,11,2021]
day, month, year = int(day), int(month), int(year)
age = current_date[2] - year

if month > current_date[1]:
    age -= 1
elif month == current_date[1] and day > current_date[0]:
    age -= 1
print(f"I am {age} years old.")

cake = (f'''
       ___{int(str(age)[-1])* 'i'}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
''')
print(cake)