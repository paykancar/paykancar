class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def disp(self):
        print(self.num1 + self.num2)


p1 = Calculator(25, 12)
p1.disp()