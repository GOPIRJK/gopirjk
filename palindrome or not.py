def isPalindrome(s):
	return s == s[::-1]
s = input("enter a string")
ans = isPalindrome(s)

if ans:
	print("palindrome")
else:
	print("Not a palindrome")
