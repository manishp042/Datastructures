n =5
val = 0 
for i in range(n, 0, -1) :
    if val==0:
        val=i
    else:
        val = val*i
print(val)
