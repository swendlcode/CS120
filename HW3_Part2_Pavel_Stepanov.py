# Tax is 5% of the subtotal
# Tip is 15% of the subtotal.
def subtotal(meal1=44, meal2=30, meal3=12, meal4=37, meal5=12):
    subtotal = meal5 + meal4 + meal3 + meal2 + meal1
    return subtotal


def tax(subtotal):
    tax = (subtotal / 100) * 5
    return tax


def tip(subtotal):
    tip = (subtotal / 100) * 15
    return tip

tax = tax(subtotal())
tip = tip(subtotal())
total = tax + tip + subtotal()


print("The subtotal was : $", subtotal())
print("The tax was : $",tax)
print("The tip was : $",tip)
print("The total was : $", total)
