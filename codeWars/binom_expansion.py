
from math import factorial as fact
from string import ascii_lowercase
import re

class Term:
    def __init__(self, sign=None, coef=None, var=None):
        if sign is None:
            sign = "+"
        if coef is None:
            coef = 1
        if var is None:
            var = {}
        self.sign = sign
        self.coef = coef
        self.var = var

    def getSign(self):
        return self.sign

    def signAdd(self, x):
        s = self.getSign()
        self.sign = "+" if x == s else "-"

    def getCoef(self):
        return self.coef

    def getVar(self):
        return self.var.copy()

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.mult_const(other)
        s = "+" if self.getSign() == other.getSign() else "-"
        c = self.getCoef() * other.getCoef()
        if int(c) == float(c):
            c = int(c)
        v = self.getVar()
        o = other.getVar()
        for i in o:
            v[i] = v.get(i, 0) + o[i]
            if v[i] == 0 and len(v) > 1:
                del v[i]
        return Term(s, c, v)

    def strVar(self):
        var = self.getVar()
        if len(var) == 0:
            return ""
        elif len(var) == 1:
            out = ""
            for i in var:
                if var[i] == 0:
                    out = ""
                elif var[i] == 1:
                    out = f"{i}"
                else:
                    out += f"{i}^{var[i]}"
        else:
            out = ""
            for i in var:
                if var[i] != 1:
                    out += f"({i}^{var[i]})"
                else:
                    out += f"({i})"
        return out

    def __repr__(self):
        return str(self)

    def mult_const(self, const):
        # print("going to multiply", self, "by", const)
        new_coef = const * self.getCoef()
        # print("new coef is", new_coef)
        const_sign = "-" if const < 0 else "+"
        new_sign = "+" if self.getSign() == const_sign else "-"
        return Term(new_sign, abs(new_coef), self.getVar())

    def power(self, n):
        print("calculating", self, "to the power", n)
        if n == 0:
            print(Term("+", 1, None))
            return Term("+", 1, None)
        new_var = self.getVar()
        for i in new_var:
            new_var[i] *= n
        print("\told var", self.getVar(), "new", new_var)
        new_coef = self.getCoef() ** n
        print("\told coef", self.getCoef(), "new", new_coef)
        new_sign = "+-"[({"-":1, "+":0}[self.getSign()]*n)%2]
        print("\told sign", self.getSign(), "new", new_sign)
        return Term(new_sign, new_coef, new_var)


    def __str__(self):
        s = "" if self.getSign() == "+" else "-"
        var = self.getVar()
        v = self.strVar()
        c = self.getCoef()
        if c == 0:
            return "0"
        elif v == "":
            return s+str(c)
        elif c == 1 and v != "":
            return s+v
        else:
            return s+str(c)+v

    def strWithSign(self):
        out = str(self)
        if self.getSign() == "+":
            out = "+"+out
        return out

    @staticmethod
    def mergeTerms(terms):
        out = str(terms[0])
        first = True
        for term in terms[1:]:
            out += term.strWithSign()
        return out



def parse_terms(terms):
    """
    given a list of terms, parses them
    """
    out = []
    for i in terms:
        var = re.search(r"[a-z]", i)
        if var is None:
            coef = int(i)
        else:
            var = var.start()
            print("index of match", var, "val:")
            try:
                coef = int(i[:var])
            except ValueError:
                coef = 1
            var = {i[var:]: 1}
        sign = "+" if abs(coef) == coef else "-"
        out.append(Term(sign, abs(coef), var))
    return out


def parse(text):
    """
    Assumes that the entered text is of the form:
    (ax + b)^n
    """
    print("text to be parsed", text)
    power = int(text[text.index("^")+1:])
    terms = text[1:text.index("^")-1]
    print(repr(power), repr(terms))
    separator = "+" if terms[1:].count("-") % 2 == 0 else "-"
    sep_index = terms[1:].index(separator)+1
    t1 = terms[:sep_index]
    t2 = terms[sep_index+1:]
    t1, t2 = parse_terms([t1, t2])
    t2.signAdd(separator)
    return power, t1, t2




def nCr(n, r):
    f = lambda x: int(fact(x))
    return int(f(n)/f(n-r)/f(r))


def expand(text):
    """
    Uses the binomial theorem.
    """
    n, t1, t2 = parse(text)
    if str(t1) == "0":
        return [t2.power(n)]
    elif str(t2) == "0":
        return [t1.power(n)]
    terms = []
    print("expression shall have", n+1, "terms")
    for i in range(0, n+1):
        print("\tterm", i+1)
        terms.append(t1.power(n-i) * t2.power(i) * nCr(n, i))
    return Term.mergeTerms(terms)




x = Term(sign="-", coef=234, var={"x":1, "c":3})
print(x)
y = Term(sign="-", coef=1/2, var={"c":-3})
print(x*y)
z = expand("(x-1)^2")
print(z)
