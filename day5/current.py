def calculate_bill_with_elif(units):
    service_charge = 50
    total_bill = 0
    
    if units <= 100:
        total_bill = units * 50
    elif 101 <= units <= 200:
        total_bill = units * 100
    else:
        total_bill = units * 150
    
    total_bill += service_charge
    return total_bill

# Example usage:
units = int(input("Enter the number of units consumed: "))
bill = calculate_bill_with_elif(units)
print(f"Total current bill (with elif): {bill} rupees")






def calculate_bill_without_elif(units):
    service_charge = 50
    total_bill = 0
    
    if units <= 100:
        total_bill = units * 50
    if 101 <= units <= 200:
        total_bill = units * 100
    if units > 200:
        total_bill = units * 150
    
    total_bill += service_charge
    return total_bill

# Example usage:
units = int(input("Enter the number of units consumed: "))
bill = calculate_bill_without_elif(units)
print(f"Total current bill (without elif): {bill} rupees")