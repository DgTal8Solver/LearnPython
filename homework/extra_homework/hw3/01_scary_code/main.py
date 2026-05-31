def main():
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]

    a += b

    five_count = a.count(5)
    for i, value in enumerate(a):
        if value == 5: a.pop(i)

    a += c

    three_count = a.count(3)

    print("Результат работы программы:")
    print(f"Кол-во цифр 5 при первом объединении: {five_count}")
    print(f"Кол-во цифр 3 при втором объединении: {three_count}")
    print(f"Итоговый список: {a}")

if __name__ == "__main__":
    main()