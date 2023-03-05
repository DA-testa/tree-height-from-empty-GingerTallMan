# 221RDB254
# Imports
import sys
import threading
import numpy

# Function 
def compute_height(n, parents):
    # Loops in range of n
    for i in range(n):
        depth=0
        indicator=i
        while indicator!=-1:
            depth=depth+1
            indicator=parents[indicator]
        max_height=max(max_height,depth)
    return max_height
#Main
def main():
    teksts=str(input())
    if "I" in teksts:
        number=int(input())
        lists=list(map(int, input().split()))
        print(compute_height(number, lists))
    if "F" in teksts:
        vards=str(input())
        vards="test/"+str(vards)
        fails=open(vards,'r')
        number=int(fails.readline())
        lists=list(map(int, fails.readline().split()))
        fails.close()
        print(compute_height(number, lists))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()