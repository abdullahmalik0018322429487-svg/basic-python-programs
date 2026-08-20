# total cart value input lein
cart_value = float(input("Enter total cart value (PKR): "))

if cart_value > 5000:
    discount = cart_value * 0.10
    final_bill = cart_value - discount
    print("10% Discount Applied!")
    print("Discount Amount:", discount)
    print("Discounted Total:", final_bill)
else:
    print("No discount applicable")