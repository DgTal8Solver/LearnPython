def find(seq: list[int], value: int) -> int:
    """Бинарный поиск позиции в списке для указанного значения"""
    idx = (len(seq) - 1) // 2
    if idx == -1:
        return 0
    elif seq[idx] > value:
        return (idx + 1) + find(seq[(idx + 1):], value)
    elif seq[idx] < value:
        return find(seq[:idx], value)
    elif seq[idx] == value:
        return idx

def main():
    num_str = input("Количество контейнеров: ")
    if not (num_str.isdigit() and int(num_str) >= 1):
        print("Ошибка: должно быть число, не меньшее 1.")
        return
    num = int(num_str)

    check_container = lambda x: (x.isdigit() and int(x) <= 200)
    
    containers = []
    for _ in range(num):
        weight_str = input("Введите вес контейнера: ")
        if check_container(weight_str):
            containers += [int(weight_str)]
        else:
            print("Ошибка: можно число, не большее 200.")
            return
            
    weight_str = input("\nВведите вес нового контейнера: ")
    if check_container(weight_str):
        idx = find(containers, int(weight_str))
        print(f"\nНомер, который получит новый контейнер: {idx + 1}")
    else:
        print("Ошибка: можно число, не большее 200.")
        return
    
if __name__ == "__main__":
    main()