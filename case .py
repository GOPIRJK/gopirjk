s = input("Enter a string: ")
upper = False
lower = False

for char in s:
    if 'A' <= char <= 'Z':
        upper = True
    elif 'a' <= char <= 'z':
        lower = True

if lower and upper:
    print("Both lower and upper")
elif lower:
    print("Lower")
elif upper:
    print("Upper")
else:
    print("another")
