from PyQt6.QtWidgets import *
from voting_gui import *
import os

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.reset_button.clicked.connect(lambda: self.clear())
        self.vote_button.clicked.connect(lambda: self.vote())
        self.results_button.clicked.connect(lambda: self.results())

        self.votes = {'Halloween': 0, 'Christmas': 0}
        self.load_votes()

    def clear(self):
        pass

    def vote(self):
        try:
            choice = self.user_input.text().strip().title()
            if choice in self.votes:
                self.votes[choice] += 1
                self.save_votes()
            else:
                raise Exception
        except:
            print('wrong')

    def save_votes(self):
        # Save the current votes to the file
        filename = "votes.txt"
        try:
            with open(filename, "w") as file:
                for option, count in self.votes.items():
                    file.write(f"{option}:{count}\n")
        except Exception as e:
            print(f"Error saving votes: {e}")

    def results(self):
        print("votes: ", self.votes)

    def load_votes(self):
        filename = "votes.txt"
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line in file:
                        option, count = line.strip().split(":")
                        self.votes[option] = int(count)
        except Exception as e:
            print(f"Error loading votes: {e}")
