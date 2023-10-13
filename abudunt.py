n = int(input("enter a number"))
sum=0 
for i in range (1, n):
  if(n%i==0):  
   sum=sum+i
if(sum>n):
  print(n,'is Abundant Number')
else:
  print(n,'is not Abundant Number')
