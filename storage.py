"""
storage.py — сохранение и загрузка данных в JSON.
"""

import json
import os
from logger import get_logger

log = get_logger("storage")


def save_students(students: list[tuple], filename: str = "students.json") -> bool:
    """
    Сохранить список студентов в JSON файл.
    Каждый студент (кортеж) преобразуется в словарь для JSON.
    """
    try:
        data = [
            {"name": name, "age": age, "grade": grade}
            for name, age, grade in students
        ]

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        log.info(f"Сохранено {len(students)} студентов в {filename}")
        return True

    except Exception as e:
        log.error(f"Ошибка при сохранении: {e}")
        return False


def load_students(filename: str = "students.json") -> list[tuple]:
    """
    Загрузить список студентов из JSON файла.
    Возвращает список кортежей (имя, возраст, оценка).
    """
    if not os.path.exists(filename):
        log.info(f"Файл {filename} не найден")
        return []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        students = [(item["name"], item["age"], item["grade"]) for item in data]

        log.info(f"Загружено {len(students)} студентов из {filename}")
        return students

    except Exception as e:
        log.error(f"Ошибка при загрузке: {e}")
        return []