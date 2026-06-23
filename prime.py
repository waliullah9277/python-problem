# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % i == 0:
#         print(f'{num} is not a prime number.')
#         break
# else:
#     print(f'{num} is a prime number.')

num = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
prime_count = 0
not_prime_count = 0
for i in num:
    for j in range(2, i):
        if i % j == 0:
            # print(f'{i} is not a prime number.')
            not_prime_count += 1
            break
    else:
        # print(f'{i} is a prime number.')
        prime_count += 1

print('Total prime numbers:', prime_count)
print('Total not prime numbers:', not_prime_count)