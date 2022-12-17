#Question-2
#Write a Python program that accepts a word from the user and reverse it.

value_1 = input("Input a word to reverse: ")

value_2 = ""

for i in value_1:

    value_2 = i + value_2
    
print(" Original Value : ", value_1)
print(" Reversed value : ", value_2)