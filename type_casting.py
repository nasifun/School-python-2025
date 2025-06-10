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


price_str = '12.50'
price_f   = float(price_str)       # 12.50 → 12.5
tip       = price_f * 0.20         # 12.5 × 0.2 = 2.5

print(f"Tip amount: ${tip:.2f}")    # Tip amount: $2.50

total     = price_f + tip          # 12.5 + 2.5 = 15.0
message   = "Total cost (with tip): $" + str(round(total, 2))
print(message)                     # Total cost (with tip): $15.0

