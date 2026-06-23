def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым."""
    # Числа меньше или равные 1 не являются простыми
    if n <= 1:
        return False

    # 2 — единственное четное простое число
    if n == 2:
        return True

    for i in range(3, n):
        if n % i == 0:
            return False

    return True


# Примеры работы:
print(is_prime(1))  # False
print(is_prime(2))  # True
print(is_prime(17))  # True
