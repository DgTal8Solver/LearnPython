def main():
    s = input("Введите строку: ")
    first = s.find('h')
    last = s.rfind('h')
    if first != -1 and last != -1 and first < last:
        between = s[first+1:last]
        reversed_between = between[::-1]
    else:
        reversed_between = ""
    print(f"Развёрнутая последовательность между первым и последним h: {reversed_between}.")

if __name__ == "__main__":
    main()