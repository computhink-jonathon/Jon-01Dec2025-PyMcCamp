# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
import random

# a = 5
# b = 5
# if a != b:
#     print("not equal")
# else:
#     print("equal")

for count in range(10):
    num1 = random.randint(1,1000)
    print(str(count + 1) + ": " + str(num1))

print("-----------------------------")

counter = 0
counter1 = 0

while counter < 10:
    num1 = random.randint(1,1000)
    print(str(counter + 1) + ": " + str(num1))
    # counter = counter + 1
    counter += 1


# print("hello from day4")



########################################################################
# Task 1:



########################################################################
# Task 2:



########################################################################
# Additional exercises:



##### 
# print("----------Task 1a ----------")
# counter = 0
# while counter <= 9:
#     print(counter)
#     counter+=1

# print("----------Task 1b ----------")
# counter = 5
# while counter <= 32:
#     print(counter)
#     counter += 1

# print("----------Task 1c ----------")
# counter = 50
# while counter >= 1:
#     print(counter)
#     counter -= 1

# print("----------Task 2 ----------")
# counter = 0
# answer = "No ideas"
# user_answer = input("What do you call a deer with no eyes")
# while answer.lower() != user_answer.lower():
#     user_answer = input("What do you call a deer with no eyes")
#     counter += 1
# print("You took " + str(counter + 1) + " times to get the correct answer.")