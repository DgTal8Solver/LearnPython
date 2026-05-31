def check_palindrome(s: str) -> bool:
    return s == s[::-1]

def main():
    word = input("Введите слово: ")
    print(f"Слово {"не " if not check_palindrome(word) else ""}является палиндромом")

if __name__ == "__main__":
    main()