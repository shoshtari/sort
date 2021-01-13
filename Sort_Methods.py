def minimum(a):
    m=a[0]
    for i in range(len(a)):
        if a[i]<m:
            m=a[i]
    return m
def swap (s,x,y): 
    s[x], s[y] = s[y], s[x]
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
def MergeSort(a, n=-1):
    if n==-1:
        n=len(a)
    if n<2:
        return a
    i=n//2
    #if n is even then len l equal to n/2 else its equal to n/2+1
    l=a[i:]
    nl=i+n%2
    #if n is even then len r equal to n/2 else its equal to n/2-1
    r=a[:i]
    nr=n-nl
    l=MergeSort(l, nl)
    r=MergeSort(r, nr)
    p=0
    q=0
    out=[]
    while(p<nl and q<nr):
        if l[p]<r[q]:
            out.append(l[p])
            p+=1
        else:
            out.append(r[q])
            q+=1
    while(p<nl):
        out.append(l[p])
        p+=1
    while(q<nr):
        out.append(r[q])
        q+=1
    return out
def SelectionSort(a):
    out=[]
    la=len(a)
    for i in range(la):
        out.append(minimum(a))
        a.remove(out[i])
    return out
def InsertionSort(a):
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