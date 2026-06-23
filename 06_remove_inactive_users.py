def remove_inactive_users(users: list[dict]) -> list[dict]:
    """Удаляет из списка пользователей тех, у кого статус 'inactive'."""
    for user in users:
        if user["status"] == "inactive":
            users.remove(user)
    return users

user_list = [
    {"name": "Alice", "status": "active"},
    {"name": "Bob", "status": "inactive"},
    {"name": "Charlie", "status": "inactive"},
    {"name": "David", "status": "active"}
]

filtered_list = remove_inactive_users(user_list)
print(f"Остались в системе: {filtered_list}")