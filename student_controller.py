"""
student_controller.py — контроллер (Controller).
"""

from student_model import StudentModel
from student_view import StudentView
from validator import Validator
from logger import get_logger

log = get_logger("controller")


class StudentController:
    def __init__(self, model: StudentModel, view: StudentView):
        self.model = model
        self.view  = view
        self.validator = Validator()

        self.view.set_controller(self)
        self._refresh()
        log.info("StudentController запущен.")

    def add_student(self) -> None:
        raw_name, raw_age, raw_grade = self.view.get_form_data()

        ok, name = self.validator.validate_name(raw_name)
        if not ok:
            self.view.show_error(name)
            return

        ok, age = self.validator.validate_age(raw_age)
        if not ok:
            self.view.show_error(age)
            return

        ok, grade = self.validator.validate_grade(raw_grade)
        if not ok:
            self.view.show_error(grade)
            return

        self.model.add(name, age, grade)
        self.view.clear_form()
        self._refresh()

    def delete_student(self) -> None:
        idx = self.view.get_selected_index()
        if idx is None:
            self.view.show_info("Подсказка", "Выберите студента в списке.")
            return

        name = self.model.students[idx][0]
        if not self.view.ask_yes_no("Удалить?", f"Удалить «{name}»?"):
            log.info("Удаление отменено пользователем.")
            return

        try:
            self.model.remove(idx)
            self._refresh()
        except IndexError as e:
            log.critical("Критическая ошибка при удалении: %s", e)
            self.view.show_error(str(e))

    def sort_by_grade(self) -> None:
        self.model.sort_by_grade()
        self._refresh()

    def sort_by_name(self) -> None:
        self.model.sort_by_name()
        self._refresh()

    def show_tuple_info(self) -> None:
        idx = self.view.get_selected_index()
        if idx is None:
            self.view.show_info("Подсказка", "Выберите студента в списке.")
            return

        student = self.model.students[idx]
        name, age, grade = student

        info = (
            f"Кортеж: {student}\n\n"
            f"  student[0] = '{name}'\n"
            f"  student[1] = {age}\n"
            f"  student[2] = {grade}\n\n"
            f"Тип: {type(student).__name__}\n"
            f"Длина: {len(student)}"
        )
        log.info("Показана информация о кортеже: %s", student)
        self.view.show_info("Кортеж студента", info)

    def save_data(self) -> None:
        if self.model.save_to_file():
            self.view.show_info("Сохранено", "Данные успешно сохранены в students.json")
        else:
            self.view.show_error("Ошибка при сохранении данных")

    def search_student(self, keyword: str) -> None:
        """Поиск студентов по имени."""
        results = self.model.search_by_name(keyword)
        self.view.show_search_results(results, keyword)

    def _refresh(self) -> None:
        self.view.refresh_list(self.model.get_all())
        self.view.update_stats(self.model.get_stats())