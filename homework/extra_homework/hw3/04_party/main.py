def main():
    guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
    max_guests = 6

    while True:
        print(f"Сейчас на вечеринке {len(guests)} человек: {", ".join(guests)}")
        key = input("Гость пришёл или ушёл? ").lower().replace("ё", "е")
        match key:
            case "пришел":
                guest = input("Имя гостя: ")
                if max_guests >= len(guests) + 1:
                    guests.append(guest)
                    print(f"Привет, {guest}")
                else:
                    print(f"Прости, {guest}, но мест нет.")
            case "ушел":
                guest = input("Имя гостя: ")
                if guest in guests:
                    guests.remove(guest)
                    print(f"Пока, {guest}")
                else:
                    print("Его нет на вечеринке.")
            case "пора спать":
                print("Вечеринка закончилась, все легли спать.")
                break
            case _:
                print("Не знаю, что происходит.")

if __name__ == "__main__":
    main()