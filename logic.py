from PyQt6.QtWidgets import *
from voting_gui import *
import os

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vote_button.clicked.connect(lambda: self.vote())
        self.results_button.clicked.connect(lambda: self.results())
        self.reset_button.clicked.connect(lambda: self.clear())
        self.vote_file = 'votes.txt'

        self.votes = {'Halloween': 0, 'Christmas': 0}
        self.load_votes()

    def clear(self) -> None:
        '''
        This function ensures that the self.votes dictionary and the votes.txt
        file are reset.
        '''
        try:
            self.votes = {'Halloween': 0, 'Christmas': 0}
            open(self.vote_file, "w").close()
        except Exception as e:
            print(f"Error resetting votes. {e}")
        self.results_label.setText('')
        self.user_input.setFocus()

    def vote(self) -> None:
        try:
            choice = self.user_input.text().strip().title()
            if choice in self.votes:
                self.votes[choice] += 1
                self.save_votes()
            else:
                raise Exception
            self.results_label.setText('')
        except:
            self.results_label.setText('Invalid choice.')
        self.user_input.setText('')
        self.user_input.setFocus()

    def save_votes(self) -> None:
        # Save the current votes to the file
        try:
            with open(self.vote_file, "w") as file:
                for option, count in self.votes.items():
                    file.write(f"{option}:{count}\n")
        except Exception as e:
            print(f"Error saving votes: {e}")

    def determine_outcome(self) -> str:
        '''
        This checks the values of the keys in the self.votes dictionary
        storing the votes and determines the outcome of the vote.
        :return: This returns a string describing the outcome of the vote.
        '''
        potential_winner = ''
        potential_winning_score = 0
        ties_for_1st = 0
        for key, votes in self.votes.items():
            if votes > potential_winning_score:
                potential_winner = key
                potential_winning_score = votes
        for key, votes in self.votes.items():
            if votes == potential_winning_score:
                ties_for_1st += 1
        if ties_for_1st > 1:
            outcome = 'Tie'
        else:
            outcome = potential_winner
        return outcome


    def results(self) -> None:
        '''
        This function displays the votes each candidate, the votes they have
        have accrued, and the outcome.
        '''
        outcome = self.determine_outcome()
        results_text = ''
        for key, votes in self.votes.items():
            results_text += f'{key} has {votes} votes.\n'
        if outcome == 'Tie':
            results_text += "It's a tie!"
        else:
            results_text += f'{outcome} wins!'
        self.results_label.setText(results_text)
        print("votes: ", self.votes)
        self.user_input.setText('')
        self.user_input.setFocus()

    def load_votes(self) -> None:
        '''
        This function reads the votes.txt file and loads the self.votes
        dictionary with the saved records of votes.
        '''
        try:
            if os.path.exists(self.vote_file):
                with open(self.vote_file, "r") as file:
                    for line in file:
                        option, count = line.strip().split(":")
                        self.votes[option] = int(count)
        except Exception as e:
            print(f"Error loading votes: {e}")
