
def list_of_odd_num(end: int) -> list[int]:
    return list(range(1, end + 1, 2))

def main():
    try:
        num = int(input("Введите число: "))
        if num < 1:
            print("Ошибка: число должно быть не меньше 1.")
        else:
            odd_list = list_of_odd_num(num)
            print(f"Список из нечётных чисел от одного до N: {odd_list}")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()