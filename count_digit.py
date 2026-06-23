n = int(input("Enter a number: "))
temp = n
count = 0
while temp > 0:
    digit = temp % 10
    count += 1
    temp //= 10
print(f"The number of digits in {n} is: {count}")