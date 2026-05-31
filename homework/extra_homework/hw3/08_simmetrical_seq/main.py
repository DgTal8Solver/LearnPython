def main():
    try:
        n = int(input("Кол-во чисел: "))
        seq = []
        for _ in range(n):
            seq.append(int(input("Число: ")))
    except ValueError:
        print("Ошибка: введите число")
        return

    print("Последовательность:", seq)

    add_start = 0
    for i in range(n):
        sub = seq[i:]
        if sub == sub[::-1]:
            add_start = i
            break

    to_add = seq[add_start-1::-1]
    print("Нужно приписать чисел:", len(to_add))
    print("Сами числа:", to_add)

if __name__ == "__main__":
    main()