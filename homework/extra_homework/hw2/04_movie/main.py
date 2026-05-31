def main():
    films = [
        "Крепкий орешек", "Назад в будущее", "Таксист", 
        "Леон", "Богемская рапсодия", "Город грехов", 
        "Мементо", "Отступники", "Деревня"
    ]

    try:
        num = int(input("Сколько фильмов хотите добавить? "))
        if num < 1:
            print("Ошибка: число должно быть не меньше 1.")
        else:
            my_films = []
            for i in range(num):
                name = input("Введите название фильма: ")
                if name in my_films:
                    print(f"Ошибка: Вы уже добавили фильм '{name}'")
                elif name in films:
                    my_films += [name]
                else:
                    print(f"Ошибка: фильма '{name}' у нас нет :(")
            
            print(f"Ваш список любимых фильмов: {", ".join(my_films)}")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()