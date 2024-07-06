class Counting :
    def reverseCounting(self,number):
        if number < 0:
            return 
        print(number)
        self.reverseCounting(number-1)

    def count(self, number):
        print(f"Tyring to print {number}")
        if number < 0: 
            print("No negative allowed")
            return
        print(f"Waiting for {number} - 1 to complete")
        self.count(number-1)
        print(f"Wait for {number} - 1 Completed")
        print(number)


counting = Counting()
# counting.reverseCounting(10)
print("Straight Coutning")
counting.count(5)
