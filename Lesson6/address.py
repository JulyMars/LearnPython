#address.py
def readLines(file, list1, list2):
	f = open(file, "rb")
	f.readline()
	for line in f.readlines():
		elements = line.split()
		# print(elements[0].decode("gbk"))
		# print(elements[1].decode("gbk"))
		list1.append(str(elements[0].decode("gbk")))
		list2.append(str(elements[1].decode("gbk")))
	f.close()


def main():
	list1_name = []
	list1_tele = []
	list2_name = []
	list2_email = []
	list3 = []
	readLines("teleAddressBook.txt", list1_name, list1_tele)
	readLines("emailAddressBook.txt", list2_name, list2_email)

	for name in list1_name:
		s = ''
		i = list1_name.index(name)
		s = name+"\t"+list1_tele[i]+"\t"
		if name in list2_name:
			j = list2_name.index(name)
			s = s+list2_email[j]
		else:
			s = s+"----"
		s=s+"\n"
		print("s: ",s)
		list3.append(s)

	for name in list2_name:
		if name not in list1_name:
			s = ''
			i = list2_name.index(name)
			s = name+"\t"+"----"+"\t"+list2_email[i]
		s=s+"\n"
		list3.append(s)

	f = open("addressBook.txt", "w")
	f.writelines(list3)
	f.close()

main()