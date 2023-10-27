import re

from errors import (
    InvalidRomanNumeralError,
    NotIntegerError,
    OutOfRangeError
)

# Define digit mapping
romanNumeralMap = (
    ('M',  1000),
    ('CM', 900),
    ('D',  500),
    ('CD', 400),
    ('C',  100),
    ('XC', 90),
    ('L',  50),
    ('XL', 40),
    ('X',  10),
    ('IX', 9),
    ('V',  5),
    ('IV', 4),
    ('I',  1)
)

# Define pattern to detect valid Roman numerals
romanNumeralPattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """, re.VERBOSE)


class RomanNumeral:
    """Wrapper class that represents a roman numeral"""

    def __init__(self, value: str):
        if not isinstance(value, str):
            value = str(value)
        self.value = value.upper()

    def __str__(self) -> str:
        if self.value.isdecimal():
            return self.to_roman()
        else:
            return self.value

    def __repr__(self) -> str:
        return f"RomanNumeral({str(self.value)})"

    def __int__(self):
        return self.to_arabic()

    def to_arabic(self) -> int:
        """Converts roman numeral to integer"""
        rn = self.value
        if not romanNumeralPattern.search(rn):
            raise InvalidRomanNumeralError(f"Invalid Roman numeral: {rn}")

        result = 0
        index = 0
        for numeral, integer in romanNumeralMap:
            while rn[index:index + len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result

    def to_roman(self) -> str:
        """Convert integer to Roman numeral"""
        n = int(self.value)
        if not (0 < n < 5000):
            raise OutOfRangeError("Number out of range (must be 1..4999)")
        if int(n) != n:
            raise NotIntegerError("Non-integers can't be converted")

        result = ""
        for numeral, integer in romanNumeralMap:
            while n >= integer:
                result += numeral
                n -= integer
        return result
