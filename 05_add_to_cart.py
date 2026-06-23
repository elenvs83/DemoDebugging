def add_to_cart(item_name: str, price: float, cart: list = []) -> dict:
    """Добавляет товар в корзину и возвращает состав корзины."""
    cart.append(item_name)
    return {
        "items": cart,
        "total_items": len(cart),
        "estimated_price": price * len(cart) # Упрощенный расчет для демонстрации
    }

# Сессия пользователя №1
user1 = add_to_cart("Книга по Python", 1200.0)
print(f"Пользователь 1: {user1}")

# Сессия абсолютно другого пользователя №2
user2 = add_to_cart("Смартфон", 45000.0)
print(f"Пользователь 2: {user2}")