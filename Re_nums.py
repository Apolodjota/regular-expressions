import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

re_num = r'^\+\d{1,3}[-\s]?\d{6,12}$'

class ValidadorTelefono(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validador de Teléfono Internacional")
        self.setGeometry(500, 300, 400, 200)
        self.setStyleSheet("background-color: #f0f4f7;")  # Fondo de ventana

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Ingrese un número de teléfono (+CC Número):")
        self.label.setFont(QFont("Arial", 12))
        self.label.setStyleSheet("color: #333333;")
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.inputTelefono = QLineEdit()
        self.inputTelefono.setPlaceholderText("+593 0968785821")
        self.inputTelefono.setStyleSheet("""
            padding: 8px;
            border: 2px solid #cccccc;
            border-radius: 10px;
            font-size: 14px;
        """)
        layout.addWidget(self.inputTelefono, alignment=Qt.AlignCenter)

        self.botonValidar = QPushButton("Validar Teléfono")
        self.botonValidar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.botonValidar.clicked.connect(self.validarTelefono)
        layout.addWidget(self.botonValidar, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def validarTelefono(self):
        numero = self.inputTelefono.text()
        if re.match(re_num, numero):
            QMessageBox.information(self, "Resultado", "✅ El número de teléfono es VÁLIDO.")
        else:
            QMessageBox.warning(self, "Resultado", "❌ El número de teléfono NO es válido.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ValidadorTelefono()
    ventana.show()
    sys.exit(app.exec_())









