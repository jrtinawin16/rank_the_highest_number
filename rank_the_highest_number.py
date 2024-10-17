# Give prompt to user to input 5 random numbers
# Compare random_num1, random_num2, random_num3, random_num4, & random_num5
# If random_num1 is greater than or equal to random_num2 and random_num1 is greater than or equal to random_num3
    # print random_num1
# If random_num2 is greater than or equal to random_num1 and random_num2 is greater than or equal to random_num3
    # print random_num2
# If random_num3 is greater than or equal to random_num2 and random_num3 is greater than or equal to random_num4
    # print random_num3
# If random_num4 is greater than or equal to random_num3 and random_num4 is greater than or equal to random_num5
    # print random_num4
# If random_num5 is greater than or equal to random_num4 and random_num5 is greater than or equal to random_num3
    # print random_num5

random_num1 = int(input("Please give first number: "))
random_num2 = int(input("Please give second number: "))
random_num3 = int(input("Please give third number: "))
random_num4 = int(input("Please give fourth number: "))
random_num5 = int(input("Please give fifth number: "))
def find_highest(random_num1, random_num2, random_num3, random_num4, random_num5):
    if random_num1 >= random_num2 and random_num1 >= random_num3:
        return random_num1
    if random_num2 >= random_num1 and random_num2 >= random_num3:
        return random_num2
    if random_num3 >= random_num2 and random_num3 >= random_num4:
        return random_num3
    if random_num4 >= random_num3 and random_num4 >= random_num5:
        return random_num4
    if random_num5 >= random_num4 and random_num5 >= random_num3:
        return random_num5
result = find_highest(random_num1,random_num2,random_num3,random_num4,random_num5)
print(f"The highest number is: {result}")