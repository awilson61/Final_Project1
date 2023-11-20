from PyQt6.QtWidgets import *
from voting_gui import *
import os
from PyQt6.QtGui import QPixmap


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.TITLE = 'Voting Menu - '
        self.setupUi(self)
        # Hiding Images at start
        self.or_label.hide()
        self.halloween_image.hide()
        self.christmas_image.hide()
        self.snowman_image.hide()
        self.sun_image.hide()
        # When buttons are clicked
        self.reset_button.clicked.connect(lambda: self.clear())
        self.vote_button.clicked.connect(lambda: self.vote())
        self.results_button.clicked.connect(lambda: self.results())
        self.holiday_button.clicked.connect(lambda: self.holiday_poll())
        self.season_button.clicked.connect(lambda: self.seasons_poll())
        self.votes = {'Halloween': 0, 'Christmas': 0,
                      'Summer': 0, 'Winter': 0}
        self.load_votes()



    def holiday_poll(self) -> None:
        self.title_label.setText(self.TITLE + 'Halloween or Christmas')
        self.halloween_image.show()
        self.christmas_image.show()
        self.snowman_image.hide()
        self.sun_image.hide()
        self.poll_image.hide()
        self.or_label.show()
        self.left_label.setText('Halloween')
        self.right_label.setText('Christmas')

    def seasons_poll(self) -> None:
        self.title_label.setText(self.TITLE + 'Summer or Winter')
        self.halloween_image.hide()
        self.christmas_image.hide()
        self.poll_image.hide()
        self.snowman_image.show()
        self.sun_image.show()
        self.or_label.show()
        self.left_label.setText('Summer')
        self.right_label.setText('Winter')

    def clear(self) -> None:
        pass

    def vote(self) -> None:
        try:
            choice = self.user_input.text().strip().title()
            if choice in self.votes:
                self.votes[choice] += 1
                self.save_votes()
            else:
                raise Exception
        except:
            self.exception_label.setText("Please enter in any of the things in the poll!")




    def save_votes(self) -> None:
        # Save the current votes to the file
        filename = "votes.txt"
        try:
            with open(filename, "a") as file:
                for option, count in self.votes.items():
                    file.write(f"{option}:{count}\n")
        except Exception as e:
            print(f"Error saving votes: {e}")

    def results(self) -> None:
        if self.holiday_button.isChecked():
            #FIXME
            print('merry christmas!')
        if self.season_button.isChecked():
            #FIXME
            print(f'Summer: {self.votes["Summer"]}')

        print("votes: ", self.votes)

    def load_votes(self) -> None:
        filename = "votes.txt"
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line in file:
                        option, count = line.strip().split(":")
                        self.votes[option] = int(count)
        except Exception as e:
            print(f"Error loading votes: {e}")
