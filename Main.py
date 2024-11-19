import sys

from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget,
                             QComboBox, QTabWidget, QListView, QPushButton)

from CajaColor import CajaColor
from ModeloListaTareas import ModeloTareas
from ButtonsAñadir import Buttons
from TextoLista import TextoLista

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        super().__init__()
        self.setWindowTitle("TODO")

        # Crear una lista de tareas
        self.tareas = [

        ]

        # Crear el modelo
        self.modelo = ModeloTareas(self.tareas)

        # Crear la vista
        self.lista_vista = QListView()
        self.lista_vista.setModel(self.modelo)
        self.lista_vista.setSelectionMode(QListView.SelectionMode.MultiSelection)

        # Crear un layout y agregar la vista
        layout = QVBoxLayout()
        layoutButton = Buttons()
        layoutTexto = TextoLista()
        self.BottonAddList = QPushButton("Add to list")
        layout.addWidget(self.lista_vista)
        layout.addLayout(layoutButton)
        layout.addLayout(layoutTexto)
        layout.addWidget(self.BottonAddList)


        # Crear el widget central
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()





