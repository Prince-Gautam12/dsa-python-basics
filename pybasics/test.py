# Create a class with a method that accepts a argument a number and return an array containing the table of that number.
class TableGenerator:   #class
    def generate(self, number):     #function
       table = []
       for i in range(1,11):
           table.append(i*number)
       return table     #returning a value




# create a Display class that calls TableGenerate to generate and print table of a number
class Display:
    tablegenerator = TableGenerator()     

    def show(self):
       table = self.tablegenerator.generate(2)      #method/object
       print(table)

display = Display()
display.show()      #calling a value