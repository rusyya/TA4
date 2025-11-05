from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel
from app.tasks import circle_areas_generator, email_generator, filter_string


class CircleTab(QWidget):
    def __init__(self):
        super().__init__()
        self.gen = circle_areas_generator()

        layout = QVBoxLayout()

        btn = QPushButton("Следующие 5 значений")
        btn.clicked.connect(self.generate)
        layout.addWidget(btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def generate(self):
        try:
            result = ""
            for _ in range(5):
                area = next(self.gen)
                result += f"{area:.2f}\n"
            self.output.append(result)
        except StopIteration:
            self.output.append("Генератор завершен")


class EmailTab(QWidget):
    def __init__(self):
        super().__init__()
        self.gen = email_generator()

        layout = QVBoxLayout()

        btn = QPushButton("Сгенерировать 7 email")
        btn.clicked.connect(self.generate)
        layout.addWidget(btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def generate(self):
        result = ""
        for _ in range(7):
            email = next(self.gen)
            result += f"{email}\n"
        self.output.append(result)


class FilterTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Введите числа через пробел:"))

        self.input = QLineEdit()
        layout.addWidget(self.input)

        btn = QPushButton("Отфильтровать")
        btn.clicked.connect(self.filter)
        layout.addWidget(btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def filter(self):
        try:
            result = filter_string(self.input.text())
            self.output.append(f"Результат: {result}")
        except Exception as e:
            self.output.append(f"Ошибка: {e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генераторы и фильтры")
        self.setGeometry(100, 100, 600, 400)

        tabs = QTabWidget()
        tabs.addTab(CircleTab(), "Площади кругов")
        tabs.addTab(EmailTab(), "Генератор email")
        tabs.addTab(FilterTab(), "Фильтр чисел")

        self.setCentralWidget(tabs)