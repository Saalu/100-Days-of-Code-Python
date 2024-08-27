import random
# Randomization

ran_num = random.randint(0,1)
# ran_num = random.random()
# ran_float = random.uniform(1, 10)
print(ran_num)
# print(ran_float)

if ran_num == 1:
   print("Heads")
else:
    print("Tails")