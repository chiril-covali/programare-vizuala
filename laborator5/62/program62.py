import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testare cu comutator")
        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        self.load_btn = QPushButton("Încarcă fișier")
        self.load_btn.clicked.connect(self.load_file)
        layout.addWidget(self.load_btn)

        self.question_label = QLabel("Întrebare: ...")
        layout.addWidget(self.question_label)
        self.answer_label = QLabel("Răspuns selectat: ...")
        layout.addWidget(self.answer_label)

    def load_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Selectează fișierul de întrebări", "", "Text Files (*.txt);;All Files (*)")
        if not filename:
            return
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
        except Exception as e:
            QMessageBox.critical(self, "Eroare", f"Failed to read file: {e}")
            return

        if not lines:
            QMessageBox.warning(self, "Eroare", "Fișierul este gol.")
            return

        question = lines[0]
        options = {}
        correct = None
        for line in lines[1:]:
            if line.startswith("Raspuns corect:"):
                correct = line.split(":", 1)[1].strip()
            elif any(line.startswith(prefix) for prefix in ("A:", "B:", "C:", "D:")):
                key, value = line.split(":", 1)
                options[key.strip()] = value.strip()

        if correct is None:
            QMessageBox.warning(self, "Eroare", "Nu a fost specificat niciun răspuns corect in fișier.")
            return

        # Seleție cu ajutorul unui comutator (if-elif-else pentru compatibilitate cu versiuni mai vechi de Python)
        if correct == 'A':
            selected = options.get('A', 'N/A')
        elif correct == 'B':
            selected = options.get('B', 'N/A')
        elif correct == 'C':
            selected = options.get('C', 'N/A')
        elif correct == 'D':
            selected = options.get('D', 'N/A')
        else:
            selected = "N/A"

        self.question_label.setText(f"Întrebare: {question}")
        self.answer_label.setText(f"Răspuns selectat: {selected}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
