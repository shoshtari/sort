import time
def min(a):
    m=a[0]
    for i in range(len(a)):
        if a[i]<m:
            m=a[i]
    return m
def swap (s,x,y): 
    temp = s[x]
    s[x] = s[y]
    s[y] = temp 
################
def BubbleSort(a):
    swap=0
    done=0
    i=0
    if len(a)<2:
        return a
    while not done:
        if a[i]>a[i+1]:
            a[i]=a[i]+a[i+1]
            a[i+1]=a[i]-a[i+1]
            a[i]=a[i]-a[i+1]
            swap=1
        i+=1
        if i==len(a)-1:
            if swap==0:
                done=1
            swap=0
            i=0
    return a
def MergeSort(a):
    if len(a)<2:
        return a
    i=len(a)//2
    l=a[i:]
    r=a[:i]
    l=MergeSort(l)
    r=MergeSort(r)
    p=0
    q=0
    out=[]
    ll=len(l)
    lr=len(r)
    while(p<ll and q<lr):
        if l[p]<r[q]:
            out.append(l[p])
            p+=1
        else:
            out.append(r[q])
            q+=1
    while(p<ll):
        out.append(l[p])
        p+=1
    while(q<lr):
        out.append(r[q])
        q+=1
    return out
def SelectionSort(a):
    out=[]
    la=len(a)
    for i in range(la):
        out.append(min(a))
        a.remove(out[i])
    return out
def insertion_sort(a):
	n = len(a)
	o = 0
	for i in range(n):
		val=a[i]
		j=i-1
		while j>=0 and a[j]>val:
			a[j+1]=a[j]
			j-=1 
		a[j+1]=val
	return a

def ShellSort(a, f=0):
    if len(a)<2:
        return a
    if f==0:
        f=len(a)//2
    swap=0
    done=0
    i=0
    while not done:
        if a[i]>a[i+f]:
            a[i]=a[i]+a[i+f]
            a[i+f]=a[i]-a[i+f]
            a[i]=a[i]-a[i+f]
            swap=1
        i+=1
        if i==len(a)-f:
            if swap==0:
                done=1
            swap=0
            i=0
    return a
def QuickSort(a, first=0, last=-1):
    if last==-1:
        last=len(a)-1
    i=first
    j=last
    m=i+j//2
    w=a[m]
    while i<j:
        while a[i]<w and i<m:
            i+=1
        while a[j]>w and j>m:
            j-=1
        tmp=a[i]
        a[i]=a[j]
        a[j]=tmp
        i+=1
        j-=1
    if last<j:
        QuickSort(a, first, m)
    if i<first:
        QuickSort(a, m, last)
    return a
#CocktailSort
#HeapSort
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
        func()
        last=time.perf_counter()
    execute=last-first
    return execute
def display(a, n):
    b=[]
    b.append(execute_time(ShellSort, n))
    b.append(execute_time(MergeSort, n))
    b.append(execute_time(BubbleSort, n))
    b.append(execute_time(InsertionSort, n))
    b.append(execute_time(SelectionSort, n))
    b.append(execute_time(ListGenerator(n).sort, n))
    b.append(execute_time(QuickSort, n))
    c=b.copy()
    c.sort()
    for i in range(len(a)):
        u=b.index(c[i])
        print(a[u], b[u])
a=["Shell Sort", "Merge Sort", "Bubble Sort", "Insertion Sort", "Selection Sort", "Python Sort", "Quick Sort"]
n=int(input("enter num\n"))
display(a, n)
finall=ListGenerator(n)
finall.sort()
print(finall)
