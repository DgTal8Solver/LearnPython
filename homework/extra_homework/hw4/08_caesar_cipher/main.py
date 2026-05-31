def main():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    message = input("Введите сообщение: ")
    shift = int(input("Введите сдвиг: "))
    
    encrypted = []
    for ch in message:
        if ch.lower() in alphabet:
            idx = alphabet.index(ch.lower())
            new_idx = (idx + shift) % len(alphabet)
            new_char = alphabet[new_idx]
            if ch.isupper():
                new_char = new_char.upper()
            encrypted.append(new_char)
        else:
            encrypted.append(ch)
    print("Зашифрованное сообщение:", ''.join(encrypted))

if __name__ == "__main__":
    main()