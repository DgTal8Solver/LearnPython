def del_max_elem(elems: list[int]) -> list[int]:
    max_elem = max(elems)
    return [elem for elem in elems if elem < max_elem]

def main():
    try:
        num = int(input("Количество видеокарт: "))
        if num < 1:
            print("Ошибка: число должно быть не меньше 1.")
        else:
            gpu_list = []
            for i in range(num):
                while True:
                    gen_str = input(f"{i + 1} Видеокарта: ")
                    if gen_str.isdigit():
                        gpu_list += [int(gen_str)]
                        break
                    print("Ошибка: введите целое число.")
            
            print(f"Старый список видеокарт: [ {" ".join(str(gen) for gen in gpu_list)} ]")
            new_gpu_list = del_max_elem(gpu_list)
            print(f"Новый список видеокарт: [ {" ".join(str(gen) for gen in new_gpu_list)} ]")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()