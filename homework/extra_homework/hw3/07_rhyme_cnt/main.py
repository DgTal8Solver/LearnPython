def main():
    n = int(input("Кол-во человек: "))
    k = int(input("Какое число в считалке? "))
    print(f"Значит, выбывает каждый {k}-й человек\n")

    people = list(range(1, n + 1))
    index = 0

    while len(people) > 1:
        print(f"Текущий круг людей: {people}")
        print(f"Начало счёта с номера {people[index]}")
        
        remove_index = (index + k - 1) % len(people)
        removed = people.pop(remove_index)
        print(f"Выбывает человек под номером {removed}\n")
        index = remove_index % len(people) if people else 0

    print(f"Остался человек под номером {people[0]}")

if __name__ == "__main__":
    main()