"""
main.py — точка входа в приложение.
"""

import tkinter as tk
from logger import get_logger
from student_model import StudentModel
from student_view import StudentView
from student_controller import StudentController

log = get_logger("main")


def main():
    log.info("=" * 50)
    log.info("Приложение запускается.")

    root = tk.Tk()

    model      = StudentModel()
    view       = StudentView(root)
    controller = StudentController(model, view)

    def on_close():
        log.info("Сохранение данных перед закрытием...")
        model.save_to_file()  # ← АВТОСОХРАНЕНИЕ
        log.info("Приложение закрыто пользователем.")
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    log.info("Главный цикл запущен.")
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log = get_logger("main")
        log.critical("Непредвиденная ошибка: %s", e, exc_info=True)
        raise