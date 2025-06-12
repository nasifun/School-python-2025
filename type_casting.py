# Typecasting is the process of converting a variable from one type to another.
#        str(), int(), float(), bool()

#                    string to text
number = 7
text = str(number)
print('lucky number: ' + text)

#                    integer to string
s = '10'
n = int(s)
print(n * 3)

#                    text to float


s2 = '4.2'
f2 = float(s2)
print(f2 + 1.8)

#                    Any to boolean


for x in [0, 1, "", "hello", [], [5]]:
    print(x, "→", bool(x))

#                   example two again AI

#                    1. String to text

number = 7
text = str(number)
print('lucky number: ' + text)

#                Text to integer

s = '10'
n = int(s)
print(n * 3)

#                   assignment

#                  
price_str = '12.50'
price_f = float(price_str)
tip = price_f * 0.20

print(f'tip amount: ${tip:.2f}')
total = price_f + tip
message = 'total cost (with tip): $' +str(round(total, 2))

print (message)

                         #lesson agin day 2 

#  EXPLICIT TYPE CASTING 

name = 'Nasif'	
age = 36
height = 5.9
is_student = True

age = float(age)
print(age)

height = int(height)
print(height)

is_student = str(is_student)
print(is_student)

#  IMPLICIT TYPE CASTING

x = 5
y = 2.5
x = x + y  # x is implicitly converted to float
print(x)