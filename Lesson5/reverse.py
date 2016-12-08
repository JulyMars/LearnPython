#reverse.py
def reverse(s):
	if 1 == len(s):
		return s
	return reverse(s[1:]) + s[0]

print(reverse("abc"))
print(reverse("Hello"))