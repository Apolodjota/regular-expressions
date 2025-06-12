import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import re


class EmailValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configurar la ventana principal
        self.setWindowTitle("Validador de correo en base a una expresión regular")
        self.setGeometry(300, 300, 550, 200)

        # Crear layout vertical
        layout = QVBoxLayout()

        # Etiqueta de instrucción
        self.label = QLabel("Ingrese su correo electrónico:")
        layout.addWidget(self.label)

        # Campo de entrada
        self.entry = QLineEdit()
        self.entry.setFixedWidth(300)
        layout.addWidget(self.entry, alignment=Qt.AlignCenter)

        # Etiqueta de ejemplo
        self.ejemplo_label = QLabel("Ejemplo: romer0.figu3roa@unl45.3du")
        self.ejemplo_label.setStyleSheet("color: gray; font-style: italic;")
        layout.addWidget(self.ejemplo_label, alignment=Qt.AlignCenter)

        # Botón de verificar
        self.verificar_btn = QPushButton("Verificar")
        self.verificar_btn.clicked.connect(self.verificar)
        self.verificar_btn.setFixedWidth(100)
        layout.addWidget(self.verificar_btn, alignment=Qt.AlignCenter)

        # Etiqueta de resultado
        self.resultado_label = QLabel("")
        self.resultado_label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setBold(True)
        self.resultado_label.setFont(font)
        layout.addWidget(self.resultado_label)

        # Aplicar layout a la ventana
        self.setLayout(layout)

        # Permitir que Enter active la verificación
        self.entry.returnPressed.connect(self.verificar)

    def validate_email(self, email):
        pattern = r'^[a-z0-9]+[._\-&]{1}[a-z0-9]+@[a-z0-9]+\.[a-z0-9]+$'
        return re.match(pattern, email) is not None

    def verificar(self):
        correo = self.entry.text()
        if self.validate_email(correo):
            self.resultado_label.setText("Correo válido")
            self.resultado_label.setStyleSheet("color: green;")
        else:
            self.resultado_label.setText(
                "Correo inválido - Solo se acepta dominio con la expresion regular: [a-z0-9]+[._\-&]{1}[a-z0-9]+@[a-z0-9]+\.[a-z0-9]+")
            self.resultado_label.setStyleSheet("color: red;")


def main():
    app = QApplication(sys.argv)
    validator = EmailValidator()
    validator.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



