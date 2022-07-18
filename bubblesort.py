def bubblesort(a):
    N = len(a) 
    for i in range(N):
        for j in range(0,N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
    
a = [240,20,120,11,73,5,10,100]
res = bubblesort(a)
print(res)
