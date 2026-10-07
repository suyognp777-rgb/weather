b=109
a=float(b)
print(a)
name="John"
print(f"hello {name}")

print(name.replace("John", "Doe"))
fr="hello world hy my name is john"
print(fr.find(" "))
print(fr.replace(" ", "-"))


fruits=[]
f1=input("enter fruits name: ")
fruits.append(f1)
print(fruits)



x={
    "name":"john"

}
print(x["name"])


for i in range(5):
    print(i)

f=4
while f>0:
    print(f)
    f=f-1


class emp:
    def yolo(self,name,age): 
        print("hello")
        self.name=name
        self.age=age


s=emp()
s.yolo("john", 30)