def smallest_divisor(n: int) -> int:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

def main():
    try:
        num = int(input("Введите число: "))
        if num <= 1:
            print("Ошибка: число должно быть больше 1.")
        else:
            divisor = smallest_divisor(num)
            print(f"Наименьший делитель, отличный от единицы: {divisor}")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()