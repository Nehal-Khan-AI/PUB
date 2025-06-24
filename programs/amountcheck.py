# Get purchase amount from user
purchase_amount = float(input("Enter the purchase amount: "))

# Check the value category
if purchase_amount > 1000:
    print("High value")
elif 500 <= purchase_amount <= 1000:
    print("Medium value")
else:
    print("Low value")
