"""
validator.py — проверка данных, введённых пользователем.
"""

from logger import get_logger

log = get_logger("validator")


class Validator:
    """
    Класс для валидации полей формы.
    Каждый метод возвращает (True, значение) или (False, сообщение об ошибке).
    """

    def validate_name(self, raw: str):
        name = raw.strip()
        if not name:
            log.error("Валидация имени провалена: пустая строка.")
            return False, "Введите имя студента."
        if not name.replace(" ", "").replace("-", "").isalpha():
            log.error(f"Валидация имени провалена: недопустимые символы в '{name}'.")
            return False, "Имя должно содержать только буквы."
        if len(name) < 2:
            log.error("Валидация имени провалена: слишком короткое — '%s'.", name)
            return False, "Имя слишком короткое (минимум 2 символа)."
        log.info("Имя прошло валидацию: '%s'.", name)
        return True, name

    def validate_age(self, raw: str):
        try:
            age = int(raw)
        except ValueError:
            log.error("Валидация возраста провалена: не число — '%s'.", raw)
            return False, "Возраст должен быть целым числом."
        if not (15 <= age <= 60):
            log.error("Валидация возраста провалена: вне диапазона — %d.", age)
            return False, "Возраст должен быть от 15 до 60."
        log.info("Возраст прошёл валидацию: %d.", age)
        return True, age

    def validate_grade(self, raw: str):
        try:
            grade = float(raw.replace(",", "."))
        except ValueError:
            log.error("Валидация оценки провалена: не число — '%s'.", raw)
            return False, "Оценка должна быть числом (например: 4.5)."
        if not (0.0 <= grade <= 5.0):
            log.error("Валидация оценки провалена: вне диапазона — %.1f.", grade)
            return False, "Оценка должна быть от 0.0 до 5.0."
        log.info("Оценка прошла валидацию: %.1f.", grade)
        return True, grade
