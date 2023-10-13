num=int(input("enter a number"))
length=len(str(num))
sqn=num**2
ld=sqn%pow(10,length)
if ld==num:
    print("automorphic")
else:
    print("not a automorphic")
