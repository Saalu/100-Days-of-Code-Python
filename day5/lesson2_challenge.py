# Write a code that randomly print out the name in the list
import random

friends = ["Ama", "Kwaku", "Yaw", "Joe", "Kate", "Manu", "Mary"]
# 1nd Option
ran_num = random.randint(0, 6)
print(friends[ran_num])
# 2nd Option
# print(random.choice(friends))