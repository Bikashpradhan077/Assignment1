#Question No.1
#Write a Python program to get the Fibonacci series between 0 to 50
#Input
start=int(input("Enter the starting number : "))
end=int(input("Enter the ending number : "))
x=0
y=1
sum=0
print(" Fibonacci No. is : ", start,"to" ,end )
while(sum<end):
    x=y
    y=sum
    sum=x+y
    print(y)
print(end="")


