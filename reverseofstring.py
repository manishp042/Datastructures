def reverse(a):
    my_str = ""
    for i in a:
        my_str = i+my_str
    return my_str

a = "Manish"
res = reverse(a)
print(res)
