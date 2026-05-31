def main():
    violator_songs = [
        ["World in My Eyes", 4.86],
        ["Sweetest Perfection", 4.43],
        ["Personal Jesus", 4.56],
        ["Halo", 4.9],
        ["Waiting for the Night", 6.07],
        ["Enjoy the Silence", 4.20],
        ["Policy of Truth", 4.76],
        ["Blue Dress", 4.29],
        ["Clean", 5.83]
    ]
    songs_dict = dict(violator_songs)

    try:
        count = int(input("Сколько песен выбрать? "))
        if count < 1:
            print("Ошибка: число должно быть больше 0")
            return

        total_len = 0
        for i in range(count):
            song_name = input(f"Название {i+1}-й песни: ")
            if songs_dict.get(song_name) is None:
                print(f"Ошибка: песни '{song_name}' нет в списке")
                return
            total_len += songs_dict[song_name]
        
        print(f"\nОбщее время звучания песен: {total_len:.2f} минуты")
    except ValueError:
        print("Ошибка: введите число")

if __name__ == "__main__":
    main()