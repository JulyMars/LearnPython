#pm25.py
def main():
	PM = eval(input("pm: "))	
	if PM > 75:
		print("Unhealthy. Be Careful!")
	elif PM < 35:
		print("Good. Go running!")

main()