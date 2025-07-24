
# Related to number systems


class NumberSystem():
    """
    A number belongs to a base and has a set of digits    
    """
    def __init__(self, digits, base):
        """
        digits is a list of numbers.
        Each number is less than the base    
        """
        self.digits = digits
        self.base = base
    
    def getDigits(self):
        return self.digits[:]
    
    def getBase(self):
        return self.base

    @staticmethod
    def digitsFromStr(num_str):
        """ 
        Works for base 10    
        """
        return [int(i) for i in num_str]
    
    def __str__(self):
        out = ""
        for i in self.digits:
            out += str(i) + "-"
        return out[:-1]
    
    def convertToBase(self, base):
        if self.base == base:
            return NumberSystem(self.digits, self.base)
        number = self.inBase10()
        new_digits = []
        while number != 0:
            new_digits = [number % base] + new_digits
            number = number // base
        return NumberSystem(new_digits, base)
    
    def inBase10(self):
        total = 0
        digits = self.getDigits()
        for i in range(0, len(digits)):
            total += self.getBase()**i * digits[-1-i]
        return total
    
    def increment(self):
        added = NumberSystem(self.digitsFromStr(str(self.inBase10()+1)), 10).convertToBase(self.base)
        return added
    
    def numDigits(self):
        return len(self.getDigits())
    
    def __len__(self):
        return self.numDigits()
    
    def __lt__(self, other):
        return self.inBase10() < other.inBase10()
    
    def __eq__(self, other):
        if self.getBase() == other.getBase():
            return self.getDigits() == other.getDigits()
        return self.getDigits() == other.convertToBase(self.getBase()).getDigits()


num = NumberSystem(NumberSystem.digitsFromStr("1000000"), 10)
num16 = NumberSystem([1, 4, 7], 16)
# print(num == num16)
