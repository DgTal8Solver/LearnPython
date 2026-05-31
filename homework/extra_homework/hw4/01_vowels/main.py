def main():
    vowels = set('аеёиоуыэюя')
    text = input("Введите текст: ").lower()
    found_vowels = [ch for ch in text if ch in vowels]
    print("Список гласных букв:", found_vowels)
    print("Длина списка:", len(found_vowels))

if __name__ == "__main__":
    main()