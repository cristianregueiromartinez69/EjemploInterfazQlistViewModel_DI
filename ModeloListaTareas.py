from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage


tick = QImage("tick.png")
noHecha = QImage("noHecha.png")
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
            else:
                return noHecha

    def rowCount(self, index):
        return len(self.tarefas)
