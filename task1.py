import random
import time


st = time.time()
loops = 0
for num in range(1, 10000):
    is_fluky = 0
    for factor in range(1, num):
        loops += 1
        if num % factor == 0:
            random.seed(factor)
            is_fluky += random.randint(1, num)
    if is_fluky == num:
        print("Fluky Number: " + str(num))
et = time.time()
print("total time elapsed is: " + str(et-st))
print(str(loops) + " total loops run")