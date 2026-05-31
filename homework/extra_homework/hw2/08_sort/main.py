def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    numbers = [1, 4, -3, 0, 10]
    print("Изначальный список:", numbers)

    quicksort(numbers, 0, len(numbers) - 1)
    print("Отсортированный список:", numbers)

if __name__ == "__main__":
    main()