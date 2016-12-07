#inputerr.py

def main():
	while True:
		try:
			val = int(input("please input a int num:"))
			break
		except ValueError:
			print("input error")
		except:
			print("other error")
		else:
			print("val is ")
		finally:
			print("end.");

main()