# A biometric security system needs to generate a secure PIN from a 
# user's fingerprint data. Each scanned fingerprint is converted into a unique
# number, and the system extracts the smallest prime digit from this number to enhance security checks.
# If no prime digits exist, it alerts the user. Finds the smallest prime digit (2, 3, 5 or 7) in a given number

def check_small_prime(number):
    prime = [2, 3, 5, 7]
    small_prime = -1
    while number > 0:
        digit = number % 10
        number = number // 10
        for i in prime:
            if digit == i:
                if small_prime == -1 or digit < small_prime:
                    small_prime = digit
    
    if small_prime != -1:
        return small_prime
    else:
        return "No prime digits are found in the number"

pin = int(input("Enter the pin number"))
final_result = check_small_prime(pin)
print(final_result)


#  WAP to print the sum of odd digits in a number. {input: 2355 output - 13}

num = int(input("Enter a number"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    if digit % 2 != 0:
        sum  += digit
    temp = temp // 10
print("The sum of odd digits in a number:",sum)