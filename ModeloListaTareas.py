import sys
from cProfile import label

from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QPalette, QColor, QImage
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QGridLayout)

tick = QImage("tick.png")
class ModeloTareas (QAbstractListModel):
    def __init__(self, tarefas = None):
        super().__init__()
        self.tarefas = tarefas or [] #Podemos asignar una lista vacía o algo por defecto

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            _, texto = self.tarefas[index.row()]
            return texto

        if role == Qt.ItemDataRole.DecorationRole:
            estado,_ = self.tarefas[index.row()]
            if estado:
                return tick

    def rowCount(self, index):
        return len(self.tarefas)
