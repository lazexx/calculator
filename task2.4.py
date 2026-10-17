import random

def generate_password(use_lower, use_upper, use_special, use_digits, length):
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "!@#$%^&*()_+"
    digits = "0123456789"
    allowed_chars = ""
    if use_lower:
        allowed_chars += lower_chars
    if use_upper:
        allowed_chars += upper_chars
    if use_special:
        allowed_chars += special
    if use_digits:
        allowed_chars += digits
    password = ""
    for x in range(length):
        password += random.choice(allowed_chars)
    return password

use_lower = input("Использовать строчные буквы? (да/нет) ") == "да"
use_upper = input("Использовать заглавные буквы? (да/нет) ") == "да"
use_special = input("Использовать специальные символы? (да/нет) ") == "да"
use_digits = input("Использовать цифры? (да/нет) ") == "да"
length = int(input("Введите длину пароля: "))

print(generate_password(use_lower, use_upper, use_special, use_digits, length))
