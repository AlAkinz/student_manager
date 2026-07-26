"""
student_view.py — графический интерфейс (View).
"""

import tkinter as tk
from tkinter import messagebox, simpledialog

from theme import Theme as T
from logger import get_logger

log = get_logger("view")


class StudentView:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.controller = None

        self.root.title("Менеджер студентов")
        self.root.geometry("820x650")
        self.root.resizable(False, False)
        self.root.configure(bg=T.BG)

        self._build_header()
        self._build_content()
        self._build_footer()

        log.info("StudentView инициализирован.")

    def set_controller(self, controller) -> None:
        self.controller = controller

    def _build_header(self) -> None:
        header = tk.Frame(self.root, bg=T.ACCENT, height=54)
        header.pack(fill="x")
        tk.Label(
            header,
            text="👨‍🎓  Менеджер студентов  |  Списки и кортежи",
            bg=T.ACCENT, fg="white",
            font=T.FONT_TITLE, pady=12
        ).pack()

    def _build_content(self) -> None:
        content = tk.Frame(self.root, bg=T.BG)
        content.pack(fill="both", expand=True, padx=18, pady=14)

        self._build_listbox(content)
        self._build_right_panel(content)

    def _build_listbox(self, parent) -> None:
        left = tk.Frame(parent, bg=T.BG)
        left.pack(side="left", fill="both", expand=True)

        tk.Label(left, text="Список студентов",
                 bg=T.BG, fg=T.ACCENT2, font=T.FONT_BOLD).pack(anchor="w")

        list_frame = tk.Frame(left, bg=T.PANEL)
        list_frame.pack(fill="both", expand=True, pady=(6, 0))

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            bg=T.PANEL, fg=T.TEXT,
            selectbackground=T.ACCENT,
            selectforeground="white",
            font=T.FONT_MAIN,
            bd=0, highlightthickness=0,
            activestyle="none",
            height=14,
        )
        self.listbox.pack(fill="both", expand=True, padx=8, pady=8)
        scrollbar.config(command=self.listbox.yview)

    def _build_right_panel(self, parent) -> None:
        right = tk.Frame(parent, bg=T.BG, width=260)
        right.pack(side="right", fill="y", padx=(18, 0))
        right.pack_propagate(False)

        # Форма
        tk.Label(right, text="Добавить студента",
                 bg=T.BG, fg=T.ACCENT2, font=T.FONT_BOLD).pack(anchor="w")

        form = tk.Frame(right, bg=T.PANEL)
        form.pack(fill="x", pady=(6, 12))

        self.entry_name  = self._make_field(form, "Имя и фамилия")
        self.entry_age   = self._make_field(form, "Возраст")
        self.entry_grade = self._make_field(form, "Оценка (0.0 – 5.0)")
        tk.Label(form, bg=T.PANEL, height=1).pack()

        # Статистика
        self.stats_var = tk.StringVar()
        tk.Label(right, textvariable=self.stats_var,
                 bg=T.BG, fg=T.DIM, font=T.FONT_SMALL,
                 justify="left", wraplength=230).pack(anchor="w", pady=(0, 10))

        # Кнопки основных действий
        btn_frame = tk.Frame(right, bg=T.BG)
        btn_frame.pack(fill="x")

        buttons = [
            ("➕  Добавить",        self._on_add,         T.ACCENT),
            ("🗑  Удалить",          self._on_delete,      T.RED),
            ("↕  По оценке",        self._on_sort_grade,  T.TEAL),
            ("🔤  По имени",         self._on_sort_name,   T.BLUE),
            ("🔍  Показать кортеж",  self._on_tuple_info,  T.YELLOW),
        ]
        for label, cmd, color in buttons:
            tk.Button(
                btn_frame, text=label, command=cmd,
                bg=color, fg="white", activebackground=T.ACCENT2,
                font=T.FONT_BTN, relief="flat", cursor="hand2",
                padx=8, pady=6
            ).pack(fill="x", pady=3)

        # ─── КНОПКА ПОИСКА (как все остальные, цветная) ───
        tk.Button(
            btn_frame, text="🔎  Поиск по имени", command=self._on_search,
            bg=T.YELLOW, fg="black", activebackground=T.ACCENT2,
            font=T.FONT_BTN, relief="flat", cursor="hand2",
            padx=8, pady=6
        ).pack(fill="x", pady=3)

        # ─── КНОПКА СОХРАНЕНИЯ ───
        tk.Button(
            btn_frame, text="💾  Сохранить в JSON", command=self._on_save,
            bg=T.ACCENT2, fg="white", activebackground=T.ACCENT,
            font=T.FONT_BTN, relief="flat", cursor="hand2",
            padx=8, pady=6
        ).pack(fill="x", pady=3)

    def _build_footer(self) -> None:
        tk.Label(
            self.root,
            text="Зелёный ≥ 4.5  |  Красный < 3.5  |  💾 Автосохранение при закрытии  |  🔎 Поиск по имени",
            bg=T.BG, fg=T.DIM, font=T.FONT_SMALL
        ).pack(pady=(0, 6))

    def _make_field(self, parent, label_text: str) -> tk.Entry:
        tk.Label(parent, text=label_text, bg=T.PANEL, fg=T.DIM,
                 font=T.FONT_SMALL).pack(anchor="w", padx=10, pady=(8, 0))
        entry = tk.Entry(
            parent, bg="#3a3a52", fg=T.TEXT,
            insertbackground=T.TEXT, font=T.FONT_MAIN,
            bd=0, highlightthickness=1,
            highlightcolor=T.ACCENT, highlightbackground=T.PANEL
        )
        entry.pack(fill="x", padx=10, pady=(2, 0), ipady=5)
        return entry

    def refresh_list(self, students: list[tuple]) -> None:
        self.listbox.delete(0, tk.END)
        for i, (name, age, grade) in enumerate(students):
            line = f"  {i+1:>2}. {name:<22}  {age} лет   ★{grade:.1f}"
            self.listbox.insert(tk.END, line)
            if grade >= 4.5:
                self.listbox.itemconfig(i, fg=T.GREEN)
            elif grade < 3.5:
                self.listbox.itemconfig(i, fg=T.RED)
            else:
                self.listbox.itemconfig(i, fg=T.TEXT)

    def update_stats(self, stats: dict) -> None:
        if not stats:
            self.stats_var.set("Нет студентов")
            return
        best = stats["best"]
        self.stats_var.set(
            f"Всего: {stats['count']}  |  Ср. оценка: {stats['avg_grade']:.2f}\n"
            f"Лучший: {best[0]} ({best[2]:.1f})"
        )

    def get_form_data(self) -> tuple[str, str, str]:
        return (
            self.entry_name.get(),
            self.entry_age.get(),
            self.entry_grade.get(),
        )

    def clear_form(self) -> None:
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_grade.delete(0, tk.END)

    def get_selected_index(self):
        sel = self.listbox.curselection()
        return sel[0] if sel else None

    def show_error(self, message: str) -> None:
        messagebox.showwarning("Ошибка", message)

    def show_info(self, title: str, message: str) -> None:
        messagebox.showinfo(title, message)

    def ask_yes_no(self, title: str, question: str) -> bool:
        return messagebox.askyesno(title, question)

    def get_search_keyword_from_dialog(self):
        """Открыть диалоговое окно для ввода имени поиска."""
        keyword = simpledialog.askstring(
            "Поиск студента",
            "Введите имя или часть имени для поиска:",
            parent=self.root
        )
        return keyword.strip() if keyword else None

    def show_search_results(self, results: list[tuple], keyword: str) -> None:
        """Показать результаты поиска в отдельном окне."""
        if not results:
            self.show_info("Не найдено", f"Студенты с именем «{keyword}» не найдены")
            return

        win = tk.Toplevel(self.root)
        win.title(f"Результаты поиска: {keyword}")
        win.geometry("500x400")
        win.configure(bg=T.BG)
        win.resizable(False, False)

        tk.Label(
            win, text=f"🔍 Найдено {len(results)} студентов",
            bg=T.ACCENT, fg="white", font=T.FONT_TITLE, pady=10
        ).pack(fill="x")

        frame = tk.Frame(win, bg=T.BG)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        listbox = tk.Listbox(
            frame, yscrollcommand=scrollbar.set,
            bg=T.PANEL, fg=T.TEXT, selectbackground=T.ACCENT,
            font=T.FONT_MAIN, bd=0, highlightthickness=0
        )
        listbox.pack(fill="both", expand=True)
        scrollbar.config(command=listbox.yview)

        for i, (name, age, grade) in enumerate(results):
            line = f"  {i+1:>2}. {name:<22}  {age} лет   ★{grade:.1f}"
            listbox.insert(tk.END, line)
            if grade >= 4.5:
                listbox.itemconfig(i, fg=T.GREEN)
            elif grade < 3.5:
                listbox.itemconfig(i, fg=T.RED)

        tk.Button(
            win, text="Закрыть", command=win.destroy,
            bg=T.ACCENT, fg="white", font=T.FONT_BTN,
            relief="flat", cursor="hand2", padx=20, pady=6
        ).pack(pady=10)

    def _on_add(self):
        if self.controller:
            self.controller.add_student()

    def _on_delete(self):
        if self.controller:
            self.controller.delete_student()

    def _on_sort_grade(self):
        if self.controller:
            self.controller.sort_by_grade()

    def _on_sort_name(self):
        if self.controller:
            self.controller.sort_by_name()

    def _on_tuple_info(self):
        if self.controller:
            self.controller.show_tuple_info()

    def _on_search(self):
        """Обработчик кнопки поиска — показывает диалог и ищет."""
        if not self.controller:
            return

        keyword = self.get_search_keyword_from_dialog()
        if keyword:
            self.controller.search_student(keyword)

    def _on_save(self):
        if self.controller:
            self.controller.save_data()