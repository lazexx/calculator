word = input("Загадайте слово: ").lower()
guessed = "_" * len(word)
used_letters = []
attempts = 6
while attempts > 0 and "_" in guessed:
    print(guessed)
    letter = input("Введите букву: ").lower()
    if len(letter) != 1:
        print("Введите одну букву!")
        continue
    if letter in used_letters:
        continue
    used_letters.append(letter)
    if letter in word:
        guessed_list = list(guessed)
        for i in range(len(word)):
            if word[i] == letter:
                guessed_list[i] = letter
        guessed = "".join(guessed_list)
    else:
        attempts -= 1
        print("Такой буквы нет. Количество оставшихся попыток: ", attempts)
if attempts == 0:
    print(f"Вы проиграли. Загаданное слово: {word}")
else:
    print(f"Поздравляю, вы выиграли! Загаданное слово: {word}")
