def create_multipliers() -> list:
    """Создает список из 3 функций.
    Каждая функция должна умножать переданное число на свой индекс (0, 1 или 2).
    """
    helpers = []
    for i in range(3):
        # Создаем маленькую функцию-помощника и кладем в список
        helpers.append(lambda x: x * i)
    return helpers

multipliers = create_multipliers()

print(f"Индекс 0: {multipliers[0](10)}")
print(f"Индекс 1: {multipliers[1](10)}")
print(f"Индекс 2: {multipliers[2](10)}")