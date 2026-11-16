from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
from typing import TypeVar

from interfaces import CellUpdateReaction, LoadReaction, SaveReaction
from .coordinates import coords_to_cell_id, cell_id_to_coords

class Window(QMainWindow):
    cell_update_reaction: CellUpdateReaction | None
    save_reaction: SaveReaction | None
    load_reaction: LoadReaction | None

    btn_add_row: QPushButton
    btn_remove_row: QPushButton
    btn_add_col: QPushButton
    btn_remove_col: QPushButton
    view_switcher: QComboBox

    formula_input: QLineEdit
    table: QTableWidget

    _is_updating: bool = False
    view_style: str = "values"  # "values" or "expressions"

    def __init__(
        self,
        cell_update_reaction: CellUpdateReaction | None,
        save_reaction: SaveReaction | None,
        load_reaction: LoadReaction | None,
    ):
        super().__init__()
        self.cell_update_reaction = cell_update_reaction
        self.save_reaction = save_reaction
        self.load_reaction = load_reaction

        self.setWindowTitle("Python Excel")
        self.resize(850, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Верхня панель інструментів (кнопки керування розміром таблиці та перемикач вигляду)
        toolbar_layout = QHBoxLayout()

        self.btn_add_row = QPushButton("Додати рядок")
        self.btn_remove_row = QPushButton("Видалити рядок")
        self.btn_add_col = QPushButton("Додати стовпчик")
        self.btn_remove_col = QPushButton("Видалити стовпчик")

        toolbar_layout.addWidget(self.btn_add_row)
        toolbar_layout.addWidget(self.btn_remove_row)
        toolbar_layout.addWidget(self.btn_add_col)
        toolbar_layout.addWidget(self.btn_remove_col)

        toolbar_layout.addSpacing(20)
        view_label = QLabel("Режим відображення:")
        self.view_switcher = QComboBox()
        self.view_switcher.addItems(["Показувати значення", "Показувати вирази"])
        self.view_switcher.currentIndexChanged.connect(self.on_view_style_changed)

        toolbar_layout.addWidget(view_label)
        toolbar_layout.addWidget(self.view_switcher)
        toolbar_layout.addStretch()

        main_layout.addLayout(toolbar_layout)

        # Рядок введення виразів (Formula Bar / fx панель)
        formula_layout = QHBoxLayout()
        formula_layout.setSpacing(6)

        fx_label = QLabel("<i><b>ƒ<i>x</i></b></i>")
        fx_label.setStyleSheet("""
            font-size: 14px; 
            color: #4b5563; 
            padding: 0 4px;
            font-style: italic;
        """)

        self.formula_input = QLineEdit()
        self.formula_input.setPlaceholderText(
            "Виберіть клітинку або введіть вираз (наприклад, A1+B2, mmax(1,3,4))"
        )
        self.formula_input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #d1d5db;
                border-radius: 4px;
                padding: 6px 10px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 1px solid #3b82f6;
            }
        """)

        formula_layout.addWidget(fx_label)
        formula_layout.addWidget(self.formula_input)
        main_layout.addLayout(formula_layout)

        # Таблиця
        self.table = QTableWidget(5, 5, self)
        self.setup_table_headers()
        main_layout.addWidget(self.table)

        self._is_updating = False

        # Підключення сигналів кнопок
        self.btn_add_row.clicked.connect(self.add_row)
        self.btn_remove_row.clicked.connect(self.remove_row)
        self.btn_add_col.clicked.connect(self.add_column)
        self.btn_remove_col.clicked.connect(self.remove_column)

        # Підключення сигналів таблиці та рядка формул
        self.table.currentCellChanged.connect(self.on_current_cell_changed)
        self.table.itemChanged.connect(self.on_table_item_changed)
        self.formula_input.returnPressed.connect(self.on_formula_return_pressed)

        self.create_menus()

    def setup_table_headers(self):
        """Встановлення букв для стовпчиків (A, B, C...) та чисел для рядків (1, 2, 3...)"""
        col_count = self.table.columnCount()
        row_count = self.table.rowCount()

        col_labels = []
        for i in range(col_count):
            label = ""
            n = i
            while n >= 0:
                label = chr(ord("A") + (n % 26)) + label
                n = n // 26 - 1
            col_labels.append(label)

        self.table.setHorizontalHeaderLabels(col_labels)
        row_labels = [str(i + 1) for i in range(row_count)]
        self.table.setVerticalHeaderLabels(row_labels)

    def ensure_table_size(self, rows: int, cols: int):
        need_header_update = False
        if rows > self.table.rowCount():
            self.table.setRowCount(rows)
            need_header_update = True
        if cols > self.table.columnCount():
            self.table.setColumnCount(cols)
            need_header_update = True
        if need_header_update:
            self.setup_table_headers()

    def on_view_style_changed(self, index: int):
        self.view_style = "values" if index == 0 else "expressions"
        self._is_updating = True
        for r in range(self.table.rowCount()):
            for c in range(self.table.columnCount()):
                item = self.table.item(r, c)
                if item:
                    expr = item.data(Qt.ItemDataRole.UserRole)
                    val = item.data(Qt.ItemDataRole.UserRole + 1)
                    if expr is not None:
                        if self.view_style == "values":
                            item.setText(str(val) if expr != "" else "")
                            item.setTextAlignment(
                                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
                            )
                        else:
                            item.setText(expr)
                            item.setTextAlignment(
                                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
                            )
        self._is_updating = False

    def on_current_cell_changed(self, row: int, col: int, prev_row: int, prev_col: int):
        """Коли користувач клікає на іншу клітинку, виводимо її вираз у рядок введення"""
        self._is_updating = True
        item = self.table.item(row, col)
        if item:
            expr = item.data(Qt.ItemDataRole.UserRole)
            self.formula_input.setText(expr if expr is not None else item.text())
        else:
            self.formula_input.clear()
        self._is_updating = False

    def on_formula_return_pressed(self):
        """Коли користувач натискає Enter у рядку формул"""
        if self._is_updating or not self.cell_update_reaction:
            return

        current_row = self.table.currentRow()
        current_col = self.table.currentColumn()

        if current_row < 0 or current_col < 0:
            self.table.setCurrentCell(0, 0)
            current_row, current_col = 0, 0

        cell_id = coords_to_cell_id(current_row, current_col)
        new_text = self.formula_input.text()
        self.cell_update_reaction.execute(cell_id, new_text)

    def on_table_item_changed(self, item: QTableWidgetItem):
        """Якщо текст змінили безпосередньо всередині клітинки таблиці"""
        if self._is_updating:
            return

        if not self.cell_update_reaction:
            return

        cell_id = coords_to_cell_id(item.row(), item.column())
        self.cell_update_reaction.execute(cell_id, item.text())

    def update_cell_display(self, cell_id: str, expression: str, value: int):
        """Оновлення виразу, значення та відображуваного тексту клітинки"""
        row, col = cell_id_to_coords(cell_id)
        self.ensure_table_size(row + 1, col + 1)

        self._is_updating = True
        item = self.table.item(row, col)
        if not item:
            item = QTableWidgetItem()
            self.table.setItem(row, col, item)

        item.setData(Qt.ItemDataRole.UserRole, expression)
        item.setData(Qt.ItemDataRole.UserRole + 1, value)

        if self.view_style == "values":
            item.setText(str(value) if expression != "" else "")
            item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        else:
            item.setText(expression)
            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        if self.table.currentRow() == row and self.table.currentColumn() == col:
            self.formula_input.setText(expression)

        self._is_updating = False

    def update_cell_text(self, cell_id: str, new_text: str):
        row, col = cell_id_to_coords(cell_id)
        self.ensure_table_size(row + 1, col + 1)
        self._is_updating = True
        item = self.table.item(row, col)
        if not item:
            item = QTableWidgetItem()
            self.table.setItem(row, col, item)
        item.setText(new_text)
        self._is_updating = False

    def clear_table(self):
        self._is_updating = True
        self.table.clearContents()
        self.formula_input.clear()
        self._is_updating = False

    def show_error(self, message: str):
        QMessageBox.warning(self, "Помилка", message)

    def add_row(self):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.setup_table_headers()

    def remove_row(self):
        row_count = self.table.rowCount()
        if row_count > 1:
            self.table.removeRow(row_count - 1)
            self.setup_table_headers()

    def add_column(self):
        col_position = self.table.columnCount()
        self.table.insertColumn(col_position)
        self.setup_table_headers()

    def remove_column(self):
        col_count = self.table.columnCount()
        if col_count > 1:
            self.table.removeColumn(col_count - 1)
            self.setup_table_headers()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Delete, Qt.Key.Key_Backspace):
            if self.table.hasFocus():
                row = self.table.currentRow()
                col = self.table.currentColumn()
                if row >= 0 and col >= 0 and self.cell_update_reaction:
                    cell_id = coords_to_cell_id(row, col)
                    self.cell_update_reaction.execute(cell_id, "")
                    return
        super().keyPressEvent(event)

    def create_menus(self):
        menubar = extract_or_throw(self.menuBar())

        file_menu = extract_or_throw(menubar.addMenu("Файл"))
        save_action = extract_or_throw(file_menu.addAction("Зберегти таблицю"))
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        load_action = extract_or_throw(file_menu.addAction("Відкрити таблицю"))
        load_action.setShortcut("Ctrl+O")
        load_action.triggered.connect(self.load_file)

        help_menu = extract_or_throw(menubar.addMenu("Довідка"))
        info_action = extract_or_throw(help_menu.addAction("Про виконавця"))
        info_action.triggered.connect(self.show_author_info)
        instr_action = extract_or_throw(help_menu.addAction("Інструкція"))
        instr_action.triggered.connect(self.show_help)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Зберегти файл", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_name and self.save_reaction:
            try:
                self.save_reaction.execute(file_name)
                QMessageBox.information(
                    self, "Успіх", f"Файл успішно збережено: {file_name}"
                )
            except Exception as e:
                QMessageBox.critical(
                    self, "Помилка", f"Не вдалося зберегти файл: {e}"
                )

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Відкрити файл", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_name and self.load_reaction:
            try:
                self.load_reaction.execute(file_name)
                QMessageBox.information(
                    self,
                    "Успіх",
                    f"Файл успішно завантажено: {file_name}",
                )
            except Exception as e:
                QMessageBox.critical(
                    self, "Помилка", f"Не вдалося завантажити файл: {e}"
                )

    def show_author_info(self):
        QMessageBox.information(
            self, "Про виконавицю", "Розробниця: Студентка групи К-27 Кривко Дар'я\nПроєкт: Табличний редактор\nВаріант: 4"
        )

    def show_help(self):
        QMessageBox.information(
            self,
            "Інструкція з використання",
            "1. Вводьте числа або вирази у рядок формул або клітинку (без початкового =).\n"
            "2. Підтримуються операції +, -, *, /, div, mod та функції mmax, mmin.\n"
            "3. Посилання на клітинки формату A1, B2 тощо.\n"
            "4. Використовуйте перемикач на панелі для зміни режиму (значення або вирази).",
        )

T = TypeVar("T")
def extract_or_throw(x: T | None) -> T:
    if x is None:
        raise Exception("Failed to extract value")
    return x
