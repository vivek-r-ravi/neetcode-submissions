import math

class AreaCalc:     
    def calculate(self, *args):
        if len(args) == 1:
            return round(math.pi * args[0] ** 2, 2)
        elif len(args) == 2:
            return args[0] * args[1]

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
