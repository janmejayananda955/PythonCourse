# 1. Check if a given integer is positive, negative, or zero.

num = 0
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is positive")


# 2. Find the largest of three numbers entered by the user.

num1=int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1 > num2:
    if num1 > num3:
        print(f"{num1} is greater")
    else:
        print(f"{num3} is greater")
else:
    if num2 > num3:
        print(f"{num1} is greater")
    else:
        print(f"{num3} is greater")


# 3. Determine if a given year is a leap year.

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")



# 4. Check if a number is divisible by both 3 and 5. 

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by both 3 and 5")


# 5. Accept the age of a person and decide if they are eligible to vote (age >= 18).

age = int(input("Enter a number: "))
if age >= 18:
    print(f"Age {age} is eligible to vote")
else:
    print(f"Age {age} is not eligible to vote")
  
# 6. Check if a given character is a vowel or consonant. 

charecter = input("Enter a character: ")
vowels = 'aeiouAEIOU'
i = 0
while i < len(vowels):
    if charecter == vowels[i]:
        print(f"{charecter} is a vowel")
        break
    else:
        print(f"{charecter} is a consonant")
    i += 1 



# 7. Accept a number and check if it is a two-digit number. 


num = int(input("Enter a number: "))
if num >= 10 and num < 100:
    print(f"{num} is a two-digit number")
else:
    print(f"{num} is not a two-digit number")


# 8. Given marks, assign grades: A (>=80), B (6079), C (4059), Fail (<40). 

marks = int(input("Enter marks: "))
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# 9. Accept a temperature and display whether its Cold (<20 degreesC), Warm (2030 degreesC), or Hot (>30 degreesC). 

temp = int(input("Enter a number: "))
if temp < 20:
    print("Cold")
elif temp >= 20 and temp <= 30:
    print("Warm")
elif temp > 30:
    print("Hot")
else:
    print("Invalid temperature input")


# 10. Check if a number is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
