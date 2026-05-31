def main():
    alphabet = "abcdefg"
    print(f"1: {alphabet[:]}")           # копия
    print(f"2: {alphabet[::-1]}")        # обратный порядок
    print(f"3: {alphabet[::2]}")         # каждый второй, начиная с первого
    print(f"4: {alphabet[1::2]}")        # каждый второй, начиная со второго
    print(f"5: {alphabet[:1]}")          # все до второго элемента (индекс 1)
    print(f"6: {alphabet[-1:]}")         # все начиная с конца до предпоследнего (последний)
    print(f"7: {alphabet[3:4]}")         # от 3 до 4 (не включая 4)
    print(f"8: {alphabet[-3:]}")         # последние три
    print(f"9: {alphabet[3:5]}")         # от 3 до 5 (не включая 5)
    print(f"10: {alphabet[4:2:-1]}")     # от 4 до 2 в обратном порядке

if __name__ == "__main__":
    main()