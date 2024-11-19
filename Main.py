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
            (False,"Estudiar DI"),
            (True, "Estudiar PMDM"),
            (False, "Mirar netflix"),
            (True, "mirar futbol")
        ]

        # Crear el modelo
        self.modelo = ModeloTareas(self.tareas)

        # Crear la vista
        self.lista_vista = QListView()
        self.lista_vista.setModel(self.modelo)
        self.lista_vista.setSelectionMode(QListView.SelectionMode.MultiSelection)

        # Crear un layout y agregar la vista
        layout = QVBoxLayout()
        self.layoutButton = Buttons()
        self.layoutTexto = TextoLista()
        self.bottonAddList = QPushButton("Add TODO")

        self.layoutButton.boton_añadir.clicked.connect(self.on_button_accept)
        self.layoutButton.boton_borrar.clicked.connect(self.on_button_borrar)
        self.bottonAddList.clicked.connect(self.on_botton_add_list)
        layout.addWidget(self.lista_vista)
        layout.addLayout(self.layoutButton)
        layout.addLayout(self.layoutTexto)
        layout.addWidget(self.bottonAddList)


        # Crear el widget central
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        self.show()

    def on_button_accept(self):
        pass

    def on_button_borrar(self):
        indices = self.lista_vista.selectedIndexes()
        if indices:
            for i in sorted(indices, reverse=True):
                del self.modelo.tarefas[i.row()]

            self.modelo.layoutChanged.emit()
            self.lista_vista.clearSelection()


    def on_botton_add_list(self):
       texto_añadir =  self.layoutTexto.texto.text().strip()
       if texto_añadir:
           self.modelo.tarefas.append((False, texto_añadir))
           self.modelo.layoutChanged.emit()
           self.layoutTexto.texto.clear()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()


#Todo: borrar, tenemos que detectar lo que este seleccionado para borrarlo


