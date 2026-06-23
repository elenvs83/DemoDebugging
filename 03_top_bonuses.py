# Задача: посчитать сумму бонусов для топ-менеджеров (первых 3 сотрудников из списка)
# Бонус составляет 10%

def calculate_top_bonuses(staff_salaries: list[int]) -> int:
    total_bonus = 0
    for i in range(1, 4):
        bonus = staff_salaries[i] * 0.1
        total_bonus += bonus
    return int(total_bonus)

# Список зарплат (отсортирован по убыванию)
salaries = [150000, 120000, 90000, 70000, 50000]

# Ожидаем: 10% от (150k + 120k + 90k) = 15000 + 12000 + 9000 = 36000
final_bonuses = calculate_top_bonuses(salaries)
print(f"Итого выплачено бонусов: {final_bonuses}")