num=int(input("enter a number"))
cn=num
s=0
ln=num
length=0
while(ln>0):
    ln=ln//10
    length=length+1
print("length")
while(num>0):
    ld=num%10
    s=s+(ld**length)
    num=num//10
if cn==s:
    print("arm strong number")
else:
    print("not a arm strong number")
