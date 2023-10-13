n = int(input("Enter a number "))
s = 0
for i in range(n):
    if i * (i + 1) == n:
        s = 1
        break

if s==1:
    print("Pronic number")
else:
    print("Not a Pronic number")
