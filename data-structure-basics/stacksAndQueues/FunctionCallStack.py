class FCS:
    def entry(self, num):
        print(f'In entry before func1 ')  # 2
        self.func1(num*2)  # 2*2
        print(f'In entry after func1 ')

    def func1(self, num):
        print(f'In func1 before func2 ') # 4
        self.func2(num*2) # 4*2
        print(f'In func1 after func2 ')

    def func2(self, num):
        print(f'In func2 before func3 ') # 8
        self.func3(num*2) # 8*2
        print(f'In func2 after func3 ')
        
    def func3(self, num):
        print(f'In func3 ') # 16


fcs = FCS()
print("Start ")
fcs.entry(2)
print("outside")