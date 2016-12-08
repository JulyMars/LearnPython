#growthstar.py
def createTable(principal, apr):
	for year in range(1,11):
		principal = principal * (1+apr)
		total = caculateNum(principal)
		print("%2d"%year,end="")
		print("*" * total)
	print("  0.0k    2.5k    5k")

def caculateNum(principal):
	return int(principal*4/1000.0)

def main():
	
	principal = 1000
	apr = 0.2

	createTable(principal, apr)


main()