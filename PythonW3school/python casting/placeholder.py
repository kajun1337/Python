#Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)
"""
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
""" 

price = 59
txt = f"The price is {price:.3f} dollars"
print(txt)

zomni = f"The price is {20 * 59} dollars"
print("\n",zomni)
