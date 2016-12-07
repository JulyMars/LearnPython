#pickle 腌制 (序列化)

import pickle;
import io;

lista=["a","b","c"];
listb = pickle.dumps(lista);
print(listb);

listc = pickle.loads(listb);
print(listc)

#文件存储
group1=("a","b","c")
f1=open("1.pkl","wb");
pickle.dump(group1,f1,True)
f1.close();

f2=file("1.pk1","rb")
group2=pickle.load(f2);
print (group2)
f2.close();