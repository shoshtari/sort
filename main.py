import time
from Sort_Methods import *
def ListGenerator(n):
    a=[]
    for i in range(n, 0, -1):
        a.append(i)
    return a
def execute_time(func, num):
    a=ListGenerator(num)
    try:
        first=time.perf_counter()
        func(a)
        last=time.perf_counter()
    except:
        first=time.perf_counter()
        a.sort()
        last=time.perf_counter()
    execute=last-first
    return execute
def display(n):
    b=[]
    b.append(["Shell sort", execute_time(ShellSort, n)])
    b.append(["Merge sort", execute_time(MergeSort, n)])
    b.append(["Bubble sort", execute_time(BubbleSort, n)])
    b.append(["Insertion sort", execute_time(InsertionSort, n)])
    b.append(["Selection sort", execute_time(SelectionSort, n)])
    b.append(["Quick sort", execute_time(QuickSort, n)])
    b.sort(key=lambda x:x[1])
    for i in b:
        print(i[0], i[1])
n=int(input("enter num\n"))
display(n)
finall=ListGenerator(n)
finall.sort()
#print(finall)
