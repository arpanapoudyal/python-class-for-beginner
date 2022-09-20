price = eval(input("Price of meal: "))
tip_percentage = eval(input("Tip (%): "))

tip_amount = price * tip_percentage / 100;

total_bill = price + tip_amount

print("Tip amount is ", tip_amount, '.', sep='')
print("Bill amount is ", total_bill, '.', sep='')
