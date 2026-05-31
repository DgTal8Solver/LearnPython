def merge_sorted_lists(l1: list, l2: list) -> list:
    return list(set(l1 + l2))

def main():
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 5, 6, 8, 10]
    merged = merge_sorted_lists(list1, list2)
    print(merged)

if __name__ == "__main__":
    main()