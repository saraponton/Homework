
# generate 100 numbers, print only the prime ones

import random
x=0
while (x<100):
    for x in range(100):
        value = random.randint(1,1000)
        for i in range(2, value // 2):
            if value % i == 0:
                 exit()
        print("The number", value, "is prime")


