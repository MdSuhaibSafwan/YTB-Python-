# a = 1

# if a == 10:
#     print("A is 10")
#     print("Under if statement")
# else:
#     print("A is not 10")


# print("Not under if statement")

age = input("Please share your age: ")
age = int(age)
# if age < 20:
#     print("He/She is a teenager")
# else:
#     if age > 30:
#         print("Too old")
#     else:
#         print("Not old")

if (age >= 13) and (age <= 19):
    print("He/She is a teenager")
elif age < 13:
    print("He/She is a child")
elif (age >= 25) and (age <= 35):
    print("He/She is not a student but working")
elif age > 35:
    print("He/She is retired")
else:
    print("He/She is a uni student")

