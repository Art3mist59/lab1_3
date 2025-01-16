def bubble_sort(arr, ascending=True):
    """Функция для сортировки списка с использованием алгоритма сортировки пузырьком."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Сравниваем в зависимости от направления сортировки
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def main():
    try:
        n = int(input("Введите количество чисел для сортировки: "))
        if n <= 0:
            print("Пожалуйста, введите положительное число.")
            return

        numbers = []
        for i in range(n):
            num = float(input(f"Введите число {i + 1}: "))
            numbers.append(num)

        print("Исходный список:", numbers)

        # Запрашиваем направление сортировки
        order = input(
            "Введите направление сортировки (введите 'asc' для возрастания или 'desc' для убывания): ").strip().lower()
        if order == 'asc':
            ascending = True
        elif order == 'desc':
            ascending = False
        else:
            print("Ошибка: Неверный ввод. Используйте 'asc' или 'desc'.")
            return

        bubble_sort(numbers, ascending)
        print("Отсортированный список:", numbers)

    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные числа.")


if __name__ == "__main__":
    main()