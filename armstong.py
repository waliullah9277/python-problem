n = int(input("Enter a number: "))
armstrong = 0
temp = n
while temp > 0:
    digit = temp % 10
    armstrong += digit ** 3
    temp //= 10
if n == armstrong:
    print(f"{n} is an Armstrong number.")
else:  
    print(f"{n} is not an Armstrong number.")