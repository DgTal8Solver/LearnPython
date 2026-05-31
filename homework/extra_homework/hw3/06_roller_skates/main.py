def main():
    try:
        n_skates = int(input("Кол-во коньков: "))
        skates = []
        for i in range(n_skates):
            size = int(input(f"Размер {i+1}-й пары: "))
            skates.append(size)
    except ValueError:
        print("Ошибка: Введите число")
        return

    try:
        n_people = int(input("\nКол-во людей: "))
        people = []
        for i in range(n_people):
            size = int(input(f"Размер ноги {i+1}-го человека: "))
            people.append(size)
    except ValueError:
        print("Ошибка: Введите число")
        return

    count = 0
    for size in people:
        try:
            skates.remove(size)
            count += 1
        except ValueError:
            pass

    print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {count}")

if __name__ == "__main__":
    main()