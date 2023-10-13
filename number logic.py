#add all digits in a given number 
num=int(input(" add ,enter a number"))
s=0
while(num>0):
    ld=num%10
    s=s+ld
    num=num//10
print(s)
#multiply all digits in a given number 
num=int(input("multiply, enter a number"))
m=1
while(num>0):
    ld=num%10
    m=m*ld
    num=num//10
print(m)
#length of a given number
num=int(input("length, enter a number"))
l=0
while(num>0):
    num=num//10
    l+=1
print(l)
#reverse of a given number
num=int(input("rev,enter a number"))
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)
