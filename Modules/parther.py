import random


def lottery(my_tick=1, all_tick= 100):
    r_int = random.randint(1, all_tick)
    if r_int <= my_tick:
        return True
    else:
        return False
