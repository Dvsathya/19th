num = int(input("Enter the number : "))
num1 = str(num)
len1 = len(num1)
temp = num
sum = 0
while num>0:
    rem = num%10
    arm = rem**len1
    sum = sum+arm
    num = int(num/10)
if sum == temp:
    print(temp,"is armstrong number")
else:
    print(temp,"is not armstrong")

#armstrong program

