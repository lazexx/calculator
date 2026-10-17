def print_pack_report(cakes):
    for x in range(cakes, 0, -1):
        if x % 3 == 0 and x % 5 == 0:
            print(f"{x} - расфасуем по 3 или по 5")
        elif x % 3 == 0:
            print(f"{x} - расфасуем по 3")
        elif x % 5 == 0:
            print(f"{x} - расфасуем по 5")
        else:
            print(f"{x} - не заказываем!")

print_pack_report(int(input("Введите число пирожков для заказа: ")))