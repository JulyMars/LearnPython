#fact.py
def fact(n):
	if n == 1:
		return 1
	else:
		return fact(n-1)*n

print(fact(4))
print(fact(10))