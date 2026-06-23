n = input("Enter a string: ")
emptylist = ''
for i in n:
    emptylist = i + emptylist
if n == emptylist:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')
