def main():
    input_str = input("Введите список чисел через запятую: ")
    numbers = list(map(int, input_str.split(',')))

    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Четные числа: {even_numbers}")

    max_number = min_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
    print(f"Максимальное число: {max_number}")
    print(f"Минимальное число: {min_number}")

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    sorted_numbers = bubble_sort(numbers)
    print(f"Отсортированный список: {sorted_numbers}")


if __name__ == "__main__":
    main()