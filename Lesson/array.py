#列表
students = ["zhang", "wang", "li", "zhao"]
print(students[1]);  #wang

students[1]="meng"
print(students[1]);  #meng

#元组（不可修改）
students = ("zhang", "wang", "li", "zhao");
print(students[1])

#集合
a=set("abcddefggg")
b=set("cef")

#交集
print(a&b)

#并集
print(a|b)

#差集
print(a-b)
#print(b-a)

#去重
print(set(a))


#字典 (关联数组)
info = {"name":"wang","age":30}
info["add"]="sjz";
print(info["name"])
