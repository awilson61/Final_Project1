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
        # Hiding the buttons and user inputs
        self.user_input.hide()
        self.vote_button.hide()
        self.results_button.hide()
        self.typebelow_label.hide()
        # When buttons are clicked
        self.reset_button.clicked.connect(lambda: self.clear())
        self.vote_button.clicked.connect(lambda: self.vote())
        self.results_button.clicked.connect(lambda: self.results())
        self.holiday_button.clicked.connect(lambda: self.holiday_poll())
        self.season_button.clicked.connect(lambda: self.seasons_poll())

        self.holiday_votes_dictionary = {'Halloween': 0, 'Christmas': 0}
        self.season_votes_dictionary = {'Summer': 0, 'Winter': 0}

        self.holiday_file = 'holiday_votes.txt'
        self.season_file = 'season_votes.txt'

    def when_poll_changes(self) -> None:
        """
        This function is supposed to reduce repetition in
        the code when you switch between polls.
        """
        self.poll_image.hide()
        self.or_label.show()
        self.user_input.show()
        self.vote_button.show()
        self.results_button.show()
        self.typebelow_label.show()
        self.exception_label.clear()
        self.user_input.clear()
        self.results_label.clear()
        self.load_votes()

    def holiday_poll(self) -> None:
        self.title_label.setText(self.TITLE + 'Halloween or Christmas')
        self.left_label.setText('Halloween')
        self.right_label.setText('Christmas')
        self.halloween_image.show()
        self.christmas_image.show()
        self.snowman_image.hide()
        self.sun_image.hide()
        self.when_poll_changes()

    def seasons_poll(self) -> None:
        self.title_label.setText(self.TITLE + 'Summer or Winter')
        self.left_label.setText('Summer')
        self.right_label.setText('Winter')
        self.snowman_image.show()
        self.sun_image.show()
        self.halloween_image.hide()
        self.christmas_image.hide()
        self.when_poll_changes()

    def clear(self) -> None:
        """
        This function ensures that the self.votes dictionary and the votes.txt
        file are reset.
        """
        try:
            self.holiday_votes_dictionary = {'Halloween': 0, 'Christmas': 0}
            self.season_votes_dictionary = {'Summer': 0, 'Winter': 0}
            open(self.season_file, "w").close()
            open(self.holiday_file, "w").close()
        except Exception as e:
            print(f"Error resetting votes. {e}")
        self.results_label.setText('')
        self.user_input.setFocus()

    def vote(self) -> None:
        poll_dictionary = {}
        if self.holiday_button.isChecked():
            poll_dictionary = self.holiday_votes_dictionary
        elif self.season_button.isChecked():
            poll_dictionary = self.season_votes_dictionary
        try:
            choice = self.user_input.text().strip().title()
            if choice in poll_dictionary:
                poll_dictionary[choice] += 1
                self.save_votes()
            else:
                self.user_input.clear()
                raise Exception
            self.results_label.setText('')
        except:
            self.exception_label.setText("Please choose from an item in the poll!")
            self.user_input.clear()
        self.user_input.clear()
        self.user_input.setFocus()

    def save_votes(self) -> None:
        # Save the current votes to the file
        filename = "blank.txt"
        poll_dictionary = {}
        if self.holiday_button.isChecked():
            filename = self.holiday_file
            poll_dictionary = self.holiday_votes_dictionary
        elif self.season_button.isChecked():
            filename = self.season_file
            poll_dictionary = self.season_votes_dictionary
        try:
            with open(filename, "a") as file:
                for option, count in poll_dictionary.items():
                    file.write(f"{option}:{count}\n")
        except Exception as e:
            print(f"Error saving votes: {e}")

    def determine_outcome(self) -> str:
        """
        This checks the values of the keys in the self.votes dictionary
        storing the votes and determines the outcome of the vote.
        :return: This returns a string describing the outcome of the vote.
        """
        potential_winner = ''
        potential_winning_score = 0
        ties_for_1st = 0
        poll_dictionary = {}
        if self.holiday_button.isChecked():
            poll_dictionary = self.holiday_votes_dictionary
        elif self.season_button.isChecked():
            poll_dictionary = self.season_votes_dictionary
        for key, votes in poll_dictionary.items():
            if votes > potential_winning_score:
                potential_winner = key
                potential_winning_score = votes
        for key, votes in poll_dictionary.items():
            if votes == potential_winning_score:
                ties_for_1st += 1
        if ties_for_1st > 1:
            outcome = 'Tie'
        else:
            outcome = potential_winner
        return outcome

    def results(self) -> None:
        """
        This function displays the votes each candidate, the votes they
        have accrued, and the outcome.
        """
        outcome = self.determine_outcome()
        results_text = ''
        poll_dictionary = {}
        if self.holiday_button.isChecked():
            poll_dictionary = self.holiday_votes_dictionary
            self.exception_label.clear()
        elif self.season_button.isChecked():
            poll_dictionary = self.season_votes_dictionary
            self.exception_label.clear()
        else:
            # FIXME This message needs to be displayed to the user.
            print("Choose a poll.")
            self.results_label.setText('Choose a poll.')
        if self.holiday_button.isChecked() or self.season_button.isChecked():
            for key, votes in poll_dictionary.items():
                results_text += f'{key} has {votes} votes.\n'
            if outcome == 'Tie':
                results_text += "It's a tie!"
            else:
                results_text += f'{outcome} wins!'

        self.results_label.setText(results_text)
        print("votes: ", poll_dictionary)
        self.user_input.setText('')
        self.user_input.setFocus()

    def load_votes(self) -> None:
        filename = "blank.txt"
        poll_dictionary = {}
        if self.holiday_button.isChecked():
            filename = self.holiday_file
            poll_dictionary = self.holiday_votes_dictionary
        elif self.season_button.isChecked():
            filename = self.season_file
            poll_dictionary = self.season_votes_dictionary
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line in file:
                        option, count = line.strip().split(":")
                        poll_dictionary[option] = int(count)
        except Exception as e:
            print(f"Error loading votes: {e}")
