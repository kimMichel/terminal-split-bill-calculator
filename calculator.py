print('Welcome to the bill calculator!')

total_bill = float(input('What was the total bill? $'))
tip_value = int(input('How much tip would you like to give? 10, 12, or 15? '))
number_people = int(input('How many people will split the bill? '))

value = (total_bill + (total_bill * (tip_value / 100))) / number_people

print(f'Each person should pay: ${value}')