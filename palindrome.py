num = int(input("Enter number : "))
temp = num
rev = 0
while(num >0):
    rem = num%10
    rev = rev*10 + rem
    num = int(num/10)
if temp == rev:
    print(temp,"is palindrome")
else:
    print(temp,"is not a palindrome")

#palindrome

