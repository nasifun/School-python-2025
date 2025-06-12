#Greatting User
name = input('What is your name? ')

print(f'Hello, {name}! Welcome to the program.')

#calculate birth year

age = input('How old are you? ')
age = int(age)
birth_year = 2025 - age
print(f'you were born in {birth_year}')

kids = input('do you have kids? (yes/no) ')
print(f'yes or no {kids}')

# squar a number

num_str = input('Eenter a number to square:')
num = int(num_str)
squared = num **3 
print(f'{num} squared is {squared:.2f}')

# Simple Tip Calculator
# Combine string, float, math, and output formatting.

    #prompt for the bill amount
bill_str = input('Enter your bill total: ')
bill = float(bill_str)
# prompt for the tip percentage

tip_str = input('Tip percentage (e.g., 20 for 20%): ')
tip_percentage = float(tip_str)

# calculate the tip total
tip_total = bill * tip_percentage / 100
total = bill + tip_total

#print the results
print(f'Bill: ${bill:.2f}')
print(f'tip: ${tip_percentage:.2f}%): ${tip_total:.2f}')  
print(f'Total: ${total:.2f}')


