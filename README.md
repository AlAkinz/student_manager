<details>
<summary><b>Нажмите для русской версии</b></summary>

# Student Manager

A Python desktop application with a Graphical User Interface (GUI)...
# Менеджер студентов (Student Manager)

Учебное приложение с графическим интерфейсом (GUI) для учёта и управления данными студентов, разработанное на языке Python с использованием библиотеки Tkinter. 

Проект реализован с использованием архитектурного паттерна **MVC (Model-View-Controller)**.

---

## 📌 Особенности и функционал

* **Хранение данных:** данные о студентах (Имя, Возраст, Оценка) хранятся в виде списка кортежей `[(name, age, grade), ...]`.
* **Управление записями:** добавление и удаление студентов из списка.
* **Фильтрация и сортировка:** сортировка списка по имени и по оценке, а также фильтрация по минимальному баллу.
* **Статистика:** авторасчёт средней оценки и определение лучшего студента.
* **Валидация:** проверка корректности вводимых данных с обработкой ошибок.
* **Логирование:** запись событий работы программы в локальные файлы журнала.
* **Сохранение:** поддержка сохранения и загрузки данных в формате JSON.

---

## 🏗 Структура проекта (MVC)

* `main.py` — Точка входа в приложение.
* `student_model.py` — **Model:** Логика работы с данными и списком кортежей.
* `student_view.py` — **View:** Графический интерфейс пользователя на Tkinter.
* `student_controller.py` — **Controller:** Связующее звено между интерфейсом и моделью.
* `validator.py` — Проверка корректности пользовательского ввода.
* `storage.py` — Модуль для сохранения и загрузки данных (JSON).
* `logger.py` — Система логирования событий.
* `theme.py` / `constants.py` — Константы оформления, шрифты и стили GUI.

---

## 🚀 Запуск проекта

### Требования
* Python 3.10 или выше (Tkinter входит в стандартную библиотеку Python).

### Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone [https://github.com/ВАШ_ЛОГИН/student_manager.git](https://github.com/ВАШ_ЛОГИН/student_manager.git)
   cd student_manager

  ## Запускать через:
   python main.py
</details>

<details>
<summary><b>Click here for English Version</b></summary>

# Student Manager

A Python desktop application with a Graphical User Interface (GUI)...


# Student Manager

A Python desktop application with a Graphical User Interface (GUI) built using **Tkinter** for managing and tracking student records.

The project follows the **MVC (Model-View-Controller)** architectural pattern to maintain clean and modular code separation.

---

## 📌 Features

* **Data Structure:** Student records are represented as a list of tuples `[(name, age, grade), ...]`.
* **CRUD Operations:** Easily add and remove student records.
* **Filtering & Sorting:** Sort students by name or grade; filter by minimum grade threshold.
* **Statistics:** Automated calculation of the average grade and identifying top-performing students.
* **Data Validation:** Input validation with error handling for user data entry.
* **Event Logging:** Built-in logger that records system events to log files.
* **Persistence:** Support for saving and loading data in JSON format.

---

## 🏗 Project Architecture (MVC)

* `main.py` — Application entry point.
* `student_model.py` — **Model:** Handles data logic and operations on the tuple list.
* `student_view.py` — **View:** Tkinter-based user interface.
* `student_controller.py` — **Controller:** Connects the View events with Model operations.
* `validator.py` — Input data verification and error checking.
* `storage.py` — JSON storage management.
* `logger.py` — Application event logging system.
* `theme.py` / `constants.py` — UI theme settings, colors, and fonts.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+ (Tkinter is included in standard Python installations).

### Installation & Execution

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/student_manager.git](https://github.com/YOUR_USERNAME/student_manager.git)
   cd student_manager
## Run the application:
python main.py

</details>
