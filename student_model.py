"""
student_model.py — модель данных.
"""

from logger import get_logger
from storage import save_students, load_students

log = get_logger("model")


class StudentModel:
    def __init__(self):
        loaded = load_students()
        if loaded:
            self.students = loaded
            log.info(f"Загружено {len(self.students)} студентов из JSON")
        else:
            self.students = [
                ("Алия Бекова",     19, 4.5),
                ("Дамир Сейтов",    21, 3.8),
                ("Жанна Мусина",    20, 4.9),
                ("Арман Нуров",     22, 3.2),
                ("Сабина Касымова", 19, 4.1),
            ]
            log.info("StudentModel создан со стартовыми данными")

    def add(self, name: str, age: int, grade: float) -> tuple:
        student = (name, age, grade)
        self.students.append(student)
        log.info("Добавлен студент: %s", student)
        return student

    def remove(self, index: int) -> tuple:
        if index < 0 or index >= len(self.students):
            log.error("Неверный индекс для удаления: %d", index)
            raise IndexError(f"Индекс {index} выходит за пределы списка.")
        removed = self.students.pop(index)
        log.info("Удалён студент: %s", removed)
        return removed

    def sort_by_grade(self) -> None:
        sorted_list = sorted(self.students, key=lambda s: s[2], reverse=True)
        self.students.clear()
        self.students.extend(sorted_list)
        log.info("Список отсортирован по оценке.")

    def sort_by_name(self) -> None:
        sorted_list = sorted(self.students, key=lambda s: s[0])
        self.students.clear()
        self.students.extend(sorted_list)
        log.info("Список отсортирован по имени.")

    def get_all(self) -> list[tuple]:
        return list(self.students)

    def get_stats(self) -> dict:
        if not self.students:
            return {}
        grades = [s[2] for s in self.students]
        ages   = [s[1] for s in self.students]
        best   = max(self.students, key=lambda s: s[2])
        return {
            "count":     len(self.students),
            "avg_grade": sum(grades) / len(grades),
            "avg_age":   sum(ages)   / len(ages),
            "best":      best,
        }

    def save_to_file(self) -> bool:
        return save_students(self.students)

    def search_by_name(self, keyword: str) -> list[tuple]:
        """Поиск студентов по имени (частичное совпадение, без учёта регистра)."""
        if not keyword or not keyword.strip():
            return self.students

        keyword_lower = keyword.strip().lower()
        results = []
        for student in self.students:
            name = student[0].lower()
            if keyword_lower in name:
                results.append(student)

        log.info(f"Поиск '{keyword}': найдено {len(results)} студентов")
        return results