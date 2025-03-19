import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QPushButton, QButtonGroup, QMessageBox
from PyQt5.QtGui import QPixmap

# Exemplu de date de test
questions = [
    {
        "text": "Care este capitala Franței?",
        "image": "",  # fără ilustrație
        "options": ["Paris", "Lyon", "Marseille"],
        "correct": 0
        },
        {
        "text": "Identificați obiectul din imagine:",
        "image": "/Users/covali/Desktop/programare-vizuala-main/laborator5/63/imagine.jpg",
        "options": ["Bicicletă", "Mașină"],
        "correct": 1
        },
    # ...alte întrebări...
]

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testare cu ilustrație")
        self.current_question = 0
        self.initUI()
        self.load_question()

    def initUI(self):
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.layout = QVBoxLayout(self.central)
        
        self.lblQuestion = QLabel()
        self.layout.addWidget(self.lblQuestion)
        
        self.lblImage = QLabel()
        self.layout.addWidget(self.lblImage)
        
        self.optionsGroup = QButtonGroup(self)
        self.optionsLayout = QVBoxLayout()
        self.layout.addLayout(self.optionsLayout)
        
        self.btnNext = QPushButton("Next")
        self.btnNext.clicked.connect(self.check_answer)
        self.layout.addWidget(self.btnNext)
    
    def load_question(self):
        # Resetează opțiunile anterioare
        for i in reversed(range(self.optionsLayout.count())):
            widget = self.optionsLayout.itemAt(i).widget()
            if widget:
                self.optionsLayout.removeWidget(widget)
                widget.deleteLater()
        self.optionsGroup = QButtonGroup(self)
        
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.lblQuestion.setText(q["text"])
            
            # Încarcă imaginea dacă există
            if q.get("image"):
                pixmap = QPixmap(q["image"])
                if not pixmap.isNull():
                    self.lblImage.setPixmap(pixmap.scaledToWidth(300))
                else:
                    self.lblImage.clear()
            else:
                self.lblImage.clear()
            
            # Creează opțiunile
            for index, option in enumerate(q["options"]):
                rb = QRadioButton(option)
                self.optionsGroup.addButton(rb, index)
                self.optionsLayout.addWidget(rb)
        else:
            QMessageBox.information(self, "Test finalizat", "Ați completat testul!")
            self.close()
    
    def check_answer(self):
        selected = self.optionsGroup.checkedId()
        if selected == -1:
            QMessageBox.warning(self, "Avertisment", "Selectați o opțiune!")
            return
        
        correct = questions[self.current_question]["correct"]
        if selected == correct:
            QMessageBox.information(self, "Corect", "Răspuns corect!")
        else:
            QMessageBox.information(self, "Greșit", "Răspuns greșit!")
        
        self.current_question += 1
        self.load_question()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec_())
