def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = input("enter the string: ")
print("The original string is : ", end="")
print(s)

print("mirror image is : ", end="")
print(reverse(s))
