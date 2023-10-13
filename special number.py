num=int(input("enter a number"))
s=0
m=1
cn=num
while(num>0):
    ld=num%10
    s=s+ld
    m=m*ld
    num=num//10
if cn==s+m :
    print("num is special number")
else:
    print("num is not a special number")
