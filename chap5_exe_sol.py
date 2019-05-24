# calculator.py
class Calculator:
    def __init__(self, lst):
        self.lst = lst

    def getTotal(self):
        return sum(self.lst)

    def avg(self):
        return self.getTotal()/len(self.lst)

if __name__ == "__main__":
    print('Hello World')
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.getTotal())
    print(cal1.avg())

    cal1 = Calculator([6,7,8,9,10])
    print(cal1.getTotal())
    print(cal1.avg())

# main.py
from calculator import Calculator
cal1 = Calculator([1,2,3,4,5])
print(cal1.getTotal())
