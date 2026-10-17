def from_roman(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for x in range(len(roman_string)):
        if x + 1 < len(roman_string):
            if roman[roman_string[x + 1]] > roman[roman_string[x]]:
                total -= roman[roman_string[x]]
            else:
                total += roman[roman_string[x]]
        else:
            total += roman[roman_string[x]]
    return total

def to_roman(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(values)):
        value = values[i]
        symbol = symbols[i]
        while number >= value:
            number -= value
            result += symbol
    return result


user_roman = input("Введите римские числа через пробел: ")
roman_list = user_roman.split()

for r in roman_list:
    print(f"{r} -> {from_roman(r.upper())}")

user_numbers = input("Введите обычные числа через пробел: ")
number_list = user_numbers.split()

for n in number_list:
    print(f"{n} -> {to_roman(int(n))}")
