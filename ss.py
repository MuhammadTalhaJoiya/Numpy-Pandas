import random
random.seed(3)
def randoms_num():
    for i in range(0,3):
        print(random.randint(2,8))
        print(random.randint(3,7))

randoms_num()