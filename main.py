def bubble_sort(arr):
    """Функция для сортировки списка с использованием алгоритма сортировки пузырьком."""
    n = len(arr)
    for i in range(n):
        # Флаг для отслеживания, произошли ли изменения
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем местами, если элемент больше следующего
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов, массив уже отсортирован
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
        bubble_sort(numbers)
        print("Отсортированный список:", numbers)

    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные числа.")


if __name__ == "__main__":
    main()