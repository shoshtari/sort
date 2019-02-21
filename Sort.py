import time
def min(a):
    m=a[0]
    for i in range(len(a)):
        if a[i]<m:
            m=a[i]
    return m
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
def InsertionSort(a):
    out=[]
    o=0
    for i in a:
        j=0
        while j<o and out[j]<i:
            j+=1
        out.insert(j, i)
        o+=1
    return out
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
#CocktailSort
#QuickSort
#HeapSort
def ListGen(n):
    out=[]
    for i in range(n, 0, -1):
        out.append(i)
    return out
def execute_time(func, num):
    a=ListGen(num)
    first=time.perf_counter()
    try:
        func(a)
    except:
        func()
    last=time.perf_counter()
    execute=last-first
    return execute
a=["Shell", "Merge", "Bubble", "Insertion", "Selection", "Python Sort"]
n=int(input("enter num\n"))
o=ListGen(n)
b=[]

b.append(execute_time(ShellSort, n))
b.append(execute_time(MergeSort, n))
b.append(execute_time(BubbleSort, n))
b.append(execute_time(InsertionSort, n))
b.append(execute_time(SelectionSort, n))
b.append(execute_time(ListGen(n).sort, n))


c=b.copy()
c.sort()
for i in range(len(a)):
    u=b.index(c[i])
    print(a[u])
