def main():
    try:
        data = [int(value.strip()) for value in input("Список: ")[1:-1].split(",")]

        print("Обработанный список: [", end="")
        for i in range(len(data)-1, -1, -1):
            if data[i] % 2 == 0:
                print(f"{', ' if i < len(data)-1 else ''}{data[i]}", end="")
        print("]")
    except ValueError:
        print("Ошибка: неверный формат списка. Пример: [1,2,3,4]")

if __name__ == "__main__":
    main()