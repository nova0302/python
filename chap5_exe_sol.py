# calculator.py
class Calculator:
    def __init__(self, lst):
        self.lst = lst

    def sum(self):
        total = 0;
        for n in self.lst:
            total += n
        return total

    def avg(self):
        return self.sum()/len(self.lst)

if __name__ == "__main__":
    print('Hello World')
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())

    cal1 = Calculator([6,7,8,9,10])
    print(cal1.sum())
    print(cal1.avg())

# main.py
from calculator import Calculator
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
