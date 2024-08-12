class Demo:
    def __init__(self, data,name) -> None:
        self.data = data
        self.name = name
        
    def __str__(self) -> str:
        return f'Data = {self.data}, Mera name = {self.name}'
    
    def __eq__(self, otherObject) -> bool:
        return self.name == otherObject.name and self.data == otherObject.data

    def printData(self):
        print(self.data)

demo1 = Demo(2, "Akshay")
demo1.printData()

demo2 = Demo(2, "Akshay")
demo2.printData()

print(demo1)
print(demo2)
print(demo1 == demo2)
print (demo1.__eq__(demo2))