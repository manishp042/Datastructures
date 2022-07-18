def reverse(a,start,end):
    while start < end:
        a[start],a[end] = a[end],a[start]
        start +=1
        end -=1
    return a
    
a = [240,20,120,11,73,5,10,100]
res = reverse(a,0,len(a)-1)
print(res)
