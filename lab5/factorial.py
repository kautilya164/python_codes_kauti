
# factorial of number
def factorial(n):
    sum=1
    if n==0:
        print(sum)
    else:
        for i in range(1,n+1):
            sum=sum*i
    print("the factorial of given number is ",sum)
n=int(input("enter a number "))
factorial(n)