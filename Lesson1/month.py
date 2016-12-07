#month.py
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
m = input("please input month(1-12)")
pos = (int(m)-1)*3
mstr = months[pos:pos+3]
print("month is: "+mstr+".")