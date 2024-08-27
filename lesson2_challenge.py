# Write a code that randomly print out the name in the list
import random

friends = ["Ama", "Kwaku", "Yaw", "Joe", "Kate", "Manu", "Mary"]

ran_num = random.randint(0, 6)

index_friends = friends[ran_num]
print(index_friends)