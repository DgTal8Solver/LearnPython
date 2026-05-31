def sum_of_digits(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def count_of_digits(n: int) -> int:
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def main():
    try:
        num = int(input("Введите число: "))
        if num < 0:
            print("Ошибка: число должно быть положительным.")
        else:
            s = sum_of_digits(num)
            c = count_of_digits(num)
            diff = s - c
            print(f"\nСумма чисел: {s}")
            print(f"Количество цифр в числе: {c}")
            print(f"Разность суммы и количества цифр: {diff}")
    except ValueError:
        print("Ошибка: введено некорректное значение. Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()