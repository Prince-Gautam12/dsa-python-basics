class DataTypes :
    myStr = "Hello World!"
    myInt = 201
    myList = ["apple", "banana", "cherry"]


    def getMyStr(self):
        return  self.myStr
    
    def setMyStr(self, value):
        self.myStr = value

    def getMyInt(self):
        return  self.myInt
    
    def setMyInt(self, value):
        self.myInt = value

    def getMyList(self):
        return  self.myList
    
    def setMyList(self, value):
        self.myList = value


dataType = DataTypes()
print(dataType.getMyStr())
print(dataType.getMyStr())
print(dataType.getMyStr())
print(dataType.getMyStr())

dataType.setMyStr("Prince")
print(dataType.getMyStr())
print(dataType.getMyStr())
print(dataType.getMyStr())
print(dataType.getMyStr())
print(dataType.getMyStr())

print(dataType.getMyInt())

dataType.setMyInt(420)
print(dataType.getMyInt())


print(dataType.getMyList())
print(dataType.getMyList())
print(dataType.getMyList())
print(dataType.getMyList())

dataType.setMyList(["yo", "this", "is", "new", "list"])


print(dataType.getMyList())
print(dataType.getMyList())
print(dataType.getMyList())
print(dataType.getMyList())