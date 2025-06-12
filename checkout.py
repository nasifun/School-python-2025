name          = input("Enter your name: ")                   # string
unit_price    = float(input("Unit price ($): "))             # float
quantity      = int(input("Quantity: "))                     # int
member_str    = input("Prime member? (yes/no): ").lower()    # string
is_member     = True if member_str == "yes" else False       # bool

subtotal      = unit_price * quantity
discount      = subtotal * 0.10 if is_member else 0.0
ship_fee      = 0.0 if subtotal - discount >= 50 else 5.0
total         = subtotal - discount + ship_fee

print(f"\nOrder for {name}:")
print(f"  Subtotal:       ${subtotal:.2f}")
print(f"  Member discount:${discount:.2f}")
print(f"  Shipping fee:   ${ship_fee:.2f}")
print(f"  TOTAL:          ${total:.2f}")
if is_member:
    print("Thanks for being a member—enjoy the savings!")

usd_amount   = float(input("Amount in USD: $"))
rate         = float(input("Exchange rate (1 USD → EUR): "))

eur_amount   = usd_amount * rate

print(f"{usd_amount:.2f} USD is {eur_amount:.2f} EUR at rate {rate:.4f}")
