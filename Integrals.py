from math import *


class integrals:

    def __init__(self, func):
        self.func = func

    def f(self, x):
        try:
            eval(self.func)
        except ZeroDivisionError:
            return 0
        except ValueError:
            raise ArithmeticError
        except:
            raise SyntaxError

        st1 = self.func
        symb1 = '0'
        while st1.find('**') != -1:
            if st1[self.func.find('**')+4] != ')':
                symb2 = self.func[self.func.find('**') + 5]
                symb1 = self.func[self.func.find('**') + 3]
                st1 = st1.replace('**', '', 1)
                if int(symb2) % 2 == 0 and int(symb1) % 2 != 0:
                    raise ArithmeticError
                if int(symb1) % 2 == 0:
                    continue
        if type(eval(self.func)) == complex:
            x = abs(x)
            if int(symb1) % 2 != 0:
                return -eval(self.func)
            else:
                return eval(self.func)
        return eval(self.func)



    def rect(self, a, b, m):
        h = (b - a) / m
        s = 0
        for i in range(1, m + 1):
            s += self.f(a + h * (2 * i - 1) / 2)
        return s * (b - a) / m

    def trapez(self, a, b, m):
        h = (b - a) / m
        s = self.f(a) + self.f(b)
        for i in range(1, m):
            s += 2 * self.f(a + i * h)
        return s * h / 2

    def simp(self, a, b, m):
        h = (b - a) / m
        s = self.f(a) + self.f(b)
        for i in range(1, m):
            k = 2 + 2 * (i % 2)
            s += k * self.f(a + i * h)
        return s * h / 3


func = input()
a = 0
b = 10

print('Прямоугольник = ', (integrals(func).rect(a, b, 10000)))
print('Трапеция = ', (integrals(func).trapez(a, b, 10000)))
print('Симпсон = ', (integrals(func).simp(a, b, 10000)))
