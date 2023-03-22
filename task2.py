import random
user = "yes"
while user == "yes":

    two = 0
    one = 0
    for i in range(100000):
        elephant1 = random.randint(1,6)
        elephant2 = random.randint(1,6)
        keeper = random.randint(1,6)
        if (keeper == elephant1 or keeper == elephant2) and elephant1 != elephant2:
            one += 1
        elif (keeper == elephant1 == elephant2):
            two += 1
    two /= 1000
    one /= 1000
    rtwo = round(two, 2)
    rone = round(one, 2)

    print(str(rtwo) + "% chance of the keeper finding two")
    print(str(one) + "% chance of the keeper finding just one")
    user = input("run simulation again?(yes/no):  ")