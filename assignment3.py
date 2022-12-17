#Question no.3
#Write a Python program to count the number of even and odd numbers from a series of numbers.

num=eval(input("Enter series of Numbers : "))
even=0
odd=0
for x in num:
    if not x%2:
        even+=1
    else:
        odd+=1
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)