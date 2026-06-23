from pathlib import Path


def get_file_extension(filename: str) -> str:
    """Принимает имя файла, превращает его в объект Path
    и возвращает расширение в верхнем регистре.
    """
    file_path = Path(filename)

    ext = file_path.suffix

    return ext.upper()


target_file = "report.xlsx"

result_extension = get_file_extension(target_file)

print(f"Расширение файла: {result_extension}")