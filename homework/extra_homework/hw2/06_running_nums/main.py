def shift_list(seq: list[int], shift: int) -> list[int]:
    new_seq = [0] * len(seq)
    for i, value in enumerate(seq):
        new_seq[(i + shift) % len(new_seq)] = value
    return new_seq

def main():
    shift_str = input("Сдвиг: ")
    if not (shift_str.isdigit() and int(shift_str) >= 1):
        print("Ошибка: должно быть число, не меньшее 1.")
        return
    shift = int(shift_str)

    try:
        start_list = [int(value.strip()) for value in input("Изначальный список: ")[1:-1].split(",")]
        result_list = shift_list(start_list, shift)
        print(f"Сдвинутый список: {result_list}")
    except ValueError:
        print("Ошибка: неверный формат списка. Пример: [1,2,3,4]")
    
if __name__ == "__main__":
    main()