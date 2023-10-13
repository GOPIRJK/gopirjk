num=int(input("enter a number"))
cn=num
sqn=num**2
s=0
while(sqn>0):
    ld=sqn%10
    s=s+ld
    sqn=sqn//10
if s==num:
    print("neon number")
else:
    print("not a neon number")
