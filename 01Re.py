import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

expresion = r'^01*[0+1]*$'

class ValidadorExpresion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validador de Expresión: 01*(0+1)*")
        self.setGeometry(500, 300, 400, 200)
        self.setStyleSheet("background-color: #f9f9f9;")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Ingrese una cadena de '0' y '1':")
        self.label.setFont(QFont("Arial", 12))
        self.label.setStyleSheet("color: #333;")
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.inputCadena = QLineEdit()
        self.inputCadena.setPlaceholderText("Ejemplo: 0110101")
        self.inputCadena.setStyleSheet("""
            padding: 8px;
            border: 2px solid #ccc;
            border-radius: 8px;
            font-size: 14px;
        """)
        layout.addWidget(self.inputCadena, alignment=Qt.AlignCenter)

        self.botonValidar = QPushButton("Validar Cadena")
        self.botonValidar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px;
                border: none;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.botonValidar.clicked.connect(self.validarCadena)
        layout.addWidget(self.botonValidar, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def validarCadena(self):
        cadena = self.inputCadena.text()
        if re.match(expresion, cadena):
            QMessageBox.information(self, "Resultado", "✅ La cadena es VÁLIDA según 01*(0+1)*.")
        else:
            QMessageBox.warning(self, "Resultado", "❌ La cadena NO cumple con la expresión 01*(0+1)*.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ValidadorExpresion()
    ventana.show()
    sys.exit(app.exec_())
