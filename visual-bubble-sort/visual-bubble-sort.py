import os
import time
import random

def print_list(l: list[int]):
    for element in l:
        print("| " + '#' * element)

def bubble_sort_step(l: list[int]):
    for i in range(len(l) - 1):
        if l[i] < l[i+1]:
            a = l[i]
            l[i] = l[i+1]
            l[i+1] = a
            
            return l

def is_sorted(l: list[int]):
    return all(l[i] >= l[i+1] for i in range(len(l) - 1))

def main(l: list[int]):
    os.system('clear')

    while not is_sorted(l):
        l = bubble_sort_step(l)
        print_list(l)
        time.sleep(0.5)
        os.system('clear')

if __name__ == "__main__":
    l = [random.randint(0, 10) for i in range(10)]
    main(l)
