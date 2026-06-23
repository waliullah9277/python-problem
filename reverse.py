n = int(input("Enter a number: "))
temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp //= 10
print(f"The reverse of the number is: {reverse}")