def decimal_to_rational(num: str):
    isPositive = True
    if num[0] == "-":
        isPositive = False
        num = num[1:]
    period = ""
    fraction = ""
    integer = ""
    isPeriod = False
    if "(" in num:
        array = num.split(".")
        integer = array[0]
        for e in array[1]:
            if isPeriod and e != ")":
                period += e
            if e != "(" and not isPeriod:
                fraction += e
            else:
                isPeriod = True
        denominator = ""
        for i in range(0, len(period)):
            denominator += "9"
        for i in range(0, len(fraction)):
            denominator += "0"
        if len(fraction) == 0:
            fraction = 0
        else:
            fraction = int(fraction)
        denominator = int(denominator)
        integer = int(integer)
        period = int(period)
        numerator = 0
        if fraction == 0:
            numerator = period + integer * denominator
        else:
            numerator = fraction * period - fraction + integer * denominator
    else:
        count = abs(num.find('.') - len(num)) - 1
        numerator = int(float(num) * 10 ** count)
        denominator = 10 ** count
    if isPositive:
        rational = Rational(numerator, denominator)
    else:
        rational = Rational(numerator * (-1), denominator)
    rational.reduction()
    return rational


class Rational(object):
    def __init__(self, m, n):
        if not (type(m) == int and type(n) == int and n != 0):
            raise IOError("числитель, знаменатель - целые числа, знаменатель != 0")
        if n < 0:
            self.m = -1 * m
            self.n = -1 * n
        else:
            self.m = m
            self.n = n

    def reduction(self):
        gcd = self.__gcd(self.m, self.n)
        self.m = int(self.m / gcd)
        self.n = int(self.n / gcd)

    def __gcd(self, a, b):
        if a == 0:
            return b
        return self.__gcd(b % a, a)

    def __repr__(self):
        return f"{self.m}/{self.n}"

    def __str__(self):
        return f"{self.m}/{self.n}"

    def __eq__(self, other):  # ==
        return self.m * other.n == other.m * self.n

    def __ne__(self, other):  # !=
        return self.m * other.n != other.m * self.n

    def __lt__(self, other):  # <
        return self.m * other.n < other.m * self.n

    def __le__(self, other):  # <=
        return self.m * other.n <= other.m * self.n

    def __gt__(self, other):  # >
        return self.m * other.n > other.m * self.n

    def __ge__(self, other):  # >=
        return self.m * other.n >= other.m * self.n

    def __add__(self, other):
        return Rational(self.m * other.n + other.m * self.n, self.n * other.n)

    def __sub__(self, other):
        return Rational(self.m * other.n - other.m * self.n, self.n * other.n)

    def __mul__(self, other):
        return Rational(self.m * other.m, self.n * other.n)

    def __truediv__(self, other):
        if other.m == 0:
            raise ZeroDivisionError
        return Rational(self.m * other.n, self.n * other.m)

    def __floordiv__(self, other):
        if other.m == 0:
            raise ZeroDivisionError
        return (self.m * other.n) // (other.m * self.n)

    def __mod__(self, other):
        if other.m == 0:
            raise ZeroDivisionError
        return (self.m * other.n) % (other.m * self.n)

    def to_decimal_str(self):
        numerator = abs(self.m)
        denominator = abs(self.n)
        decimal = str(numerator // denominator) + "."
        list = {}
        index = 0
        numerator = numerator % denominator
        if numerator == 0:
            return str(self.m / self.n)
        list[numerator] = index
        flag = False
        while not flag:
            if numerator == 0:
                break
            digit = numerator * 10 // denominator
            numerator = numerator * 10 - digit * denominator
            if numerator not in list:
                decimal += str(digit)
                index += 1
                list[numerator] = index
            else:
                decimal += str(digit) + ")"
                decimal = decimal[:list.get(numerator) + len(decimal[:decimal.index(".") + 1])] + "(" + decimal[
                                                        list.get(numerator) + len(decimal[:decimal.index(".") + 1]):]
                flag = True
        if self.m < 0:
            decimal = "-" + decimal
        return decimal
