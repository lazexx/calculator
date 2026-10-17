# Алфавиты
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
en = 'abcdefghijklmnopqrstuvwxyz'


# Определяем язык
def get_language(text):
    for char in text.lower():
        if char in ru:
            return 'ru'
    return 'en'


# Шифр
def encrypt(text, shift):
    lang = get_language(text)
    if lang == 'ru':
        alphabet = ru
    else:
        alphabet = en

    result = ''
    n = len(alphabet)

    for char in text:
        if char.lower() in alphabet:
            # Находим индекс буквы в алфавите
            index = alphabet.index(char.lower())
            # Сдвигаем и берем остаток, чтобы не выйти за пределы
            new_index = (index + shift) % n
            new_char = alphabet[new_index]

            # Делаем новую букву тоже заглавной
            if char.isupper():
                new_char = new_char.upper()

            result = result + new_char
        else:
            # Если это пробел или знак, просто добавляем
            result = result + char

    return result

# Запуск программы
text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))

encrypted_text = encrypt(text, shift)

print("Язык:", get_language(text))
print("Зашифровано:", encrypted_text)
