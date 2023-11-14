from PyQt6.QtWidgets import *
from voting_gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.reset_button.clicked.connect(lambda: self.clear())
        self.vote_button.clicked.connect(lambda: self.vote())
        self.results_button.clicked.connect(lambda: self.results())

    def clear(self):
        pass

    def vote(self):
        pass

    def results(self):
        pass