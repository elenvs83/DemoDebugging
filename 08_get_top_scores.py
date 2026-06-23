def get_top_scores(scores_list: list[int]) -> list[int]:
    """Сортирует результаты игроков по убыванию и возвращает топ-3."""
    sorted_scores = scores_list.sort(reverse=True)
    return sorted_scores[:3]


high_scores = [450, 1200, 300, 890, 750]

top_three = get_top_scores(high_scores)
print(f"Топ игроков: {top_three}")