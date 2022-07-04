total_bill = float(input("What was the total bill ?: $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))

bill_after_tip = ((total_bill*percentage_tip)/100) + total_bill

ppl = int(input("How many people to split the bill?: "))

print(f"Each person should pay: ${round((bill_after_tip/ppl), 2)}")