from PyQt6.QtWidgets import *
from voting_gui import *
import os
from PyQt6.QtGui import QPixmap
from re import *
from csv import *


class Logic(QMainWindow, Ui_MainWindow):
    BLANK_HOLIDAY_DICTIONARY = {'Halloween': 0, 'Christmas': 0, 'ballots': {}}
    BLANK_SEASON_DICTIONARY = {'Summer': 0, 'Winter': 0, 'ballots': {}}
    # These files allow the votes to be stored while the program isn't running.

    # TODO Delete these
    # self.holiday_file = 'holiday_votes.csv'
    # self.season_file = 'season_votes.csv'

    HOLIDAY_FILE = 'holiday_votes.csv'
    SEASON_FILE = 'season_votes.csv'

    def __init__(self) -> None:
        """
        This method initializes the appearance of the voting menu, the
        functions of the buttons, the dictionaries, and the files that store
        the votes between sessions.
        """
        super().__init__()
        self.TITLE = 'Voting Menu - '
        self.setupUi(self)
        # Hiding Images at start
        self.or_label.hide()
        self.halloween_image.hide()
        self.christmas_image.hide()
        self.snowman_image.hide()
        self.sun_image.hide()
        self.winter_button.hide()
        self.summer_button.hide()
        self.christmas_button.hide()
        self.halloween_button.hide()

        # These determine what happens when buttons are clicked.
        self.user_input.hide()
        self.vote_button.hide()
        self.results_button.hide()
        self.typebelow_label.hide()
        self.reset_button.hide()
        # When buttons are clicked
        self.reset_button.clicked.connect(lambda: self.clear())
        self.vote_button.clicked.connect(lambda: self.vote())
        self.results_button.clicked.connect(lambda: self.results())
        self.holiday_button.clicked.connect(lambda: self.holiday_poll())
        self.season_button.clicked.connect(lambda: self.seasons_poll())

        # These dictionaries store the votes while the program is running.
        self.holiday_votes_dictionary = {'Halloween': 0, 'Christmas': 0, 'ballots': {}}
        self.season_votes_dictionary = {'Summer': 0, 'Winter': 0, 'ballots': {}}

        # Creating Button Group
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.halloween_button)
        self.button_group.addButton(self.christmas_button)
        self.button_group.addButton(self.summer_button)
        self.button_group.addButton(self.winter_button)

    def clear_radio_button(self) -> None:
        """
        This function clears the radio buttons when you switch to another
        poll or when you click the vote button.
        """
        self.button_group.setExclusive(False)
        self.halloween_button.setChecked(False)
        self.christmas_button.setChecked(False)
        self.summer_button.setChecked(False)
        self.winter_button.setChecked(False)
        self.button_group.setExclusive(True)

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
        self.reset_button.show()
        self.voter_list.clear()
        self.load_votes()

    def holiday_poll(self) -> None:
        """
        This function changes the UI to permit voting for holidays.
        """
        self.title_label.setText(self.TITLE + 'Halloween or Christmas')
        self.results_label.setText('')
        self.exception_label.setText("")
        self.halloween_image.show()
        self.christmas_image.show()
        self.summer_button.hide()
        self.winter_button.hide()
        self.christmas_button.show()
        self.halloween_button.show()
        self.snowman_image.hide()
        self.sun_image.hide()
        self.clear_radio_button()
        self.load_votes()
        self.when_poll_changes()


    def seasons_poll(self) -> None:
        """
        This function changes the UI to permit voting for seasons.
        """
        self.title_label.setText(self.TITLE + 'Summer or Winter')

        self.results_label.setText('')
        self.exception_label.setText("")
        self.halloween_image.hide()
        self.christmas_image.hide()
        self.summer_button.show()
        self.winter_button.show()
        self.christmas_button.hide()
        self.halloween_button.hide()
        self.snowman_image.show()
        self.sun_image.show()
        self.clear_radio_button()
        self.load_votes()
        self.when_poll_changes()



    def clear(self) -> None:
        """
        This function ensures that the dictionaries and the vote files are reset.
        """
        # TODO Not sure if we need this: self.when_poll_changes()
        try:
            self.holiday_votes_dictionary = Logic.BLANK_HOLIDAY_DICTIONARY
            self.season_votes_dictionary = Logic.BLANK_SEASON_DICTIONARY
            # TODO ensure that the csv files are cleared with this.
            #open(self.season_file, "w").close()
            #open(self.holiday_file, "w").close()
            #TODO does this work below?
            self.season_votes_dictionary = {'Summer': 0, 'Winter': 0, 'ballots': {}}
            self.holiday_votes_dictionary = {'Halloween': 0, 'Christmas': 0, 'ballots': {}}
            self.exception_label.setText('')
        except Exception as e:
            print(f"Error resetting votes. {e}")
        self.results_label.setText('')
        self.voter_list.setText('')
        self.user_input.setFocus()


    def get_selected_radio_button_text(self) -> str:
        """
        This function grabs the text from the selected radio button and returns
        it as a string.
        :return: The text of the radio button.
        """
        if self.halloween_button.isChecked():
            return self.halloween_button.text().strip().title()
        elif self.christmas_button.isChecked():
            return self.christmas_button.text().strip().title()
        elif self.summer_button.isChecked():
            return self.summer_button.text().strip().title()
        elif self.winter_button.isChecked():
            return self.winter_button.text().strip().title()
        else:
            return ""

    def prepare_voter_name(self, name: str) -> str:
        reg_expression = r'[^a-zA-Z0-9\s]'
        name_without_special_characters = sub(reg_expression, '', name)
        return name_without_special_characters

    def vote(self) -> None:
        """
        This function ensures that the votes are stored in the correct dictionary.
        """
        poll_dictionary = {}
        self.holiday_button.setChecked(False)
        self.season_button.setChecked(False)
        if self.holiday_button.isChecked():
            poll_dictionary = self.holiday_votes_dictionary
        elif self.season_button.isChecked():
            poll_dictionary = self.season_votes_dictionary
        try:
            user_input_text = self.user_input.text().strip().title()
            if len(user_input_text.split()) < 2:
                raise ValueError
            self.exception_label.setText('')
            prepared_voter_name = self.prepare_voter_name(user_input_text)
            voter_name_key = prepared_voter_name
            choice = self.get_selected_radio_button_text()

            if poll_dictionary['ballots'].get(voter_name_key, "Has not voted") == "Has not voted":
                self.exception_label.setText('')
                poll_dictionary[choice] += 1
                poll_dictionary['ballots'][voter_name_key] = choice
                print(poll_dictionary['ballots'])

            else:
                self.exception_label.setText("You have already voted.")

            self.clear_radio_button()
            self.save_votes()
            self.user_input.clear()
            self.voter_list.clear()
            self.results_label.setText('')


        except ValueError:
            self.voter_list.setText('')
            self.exception_label.setText("Please ensure that you typed\na space between each name.")
            self.user_input.clear()
        except:
            #TODO the line below would be the easy solution to do.
            self.voter_list.setText('')
            self.exception_label.setText("Please select any of the items to vote!")
            #TODO Theres a lgoical error in these lines of code when the exception occurs.
            #if self.holiday_button.setChecked(True):
                #self.exception_label.setText("Please choose a holiday.")
            #elif self.season_button.setChecked(True):
                #self.exception_label.setText("Please choose a season.")
            self.user_input.clear()
        self.results_label.setText('')
        self.user_input.clear()
        self.user_input.setFocus()

    def save_votes(self) -> None:
        """
        This function ensures that the votes are saved to the correct file.
        """
        filename = "blank.txt"
        poll_dictionary = {}
        if self.holiday_button.isChecked():
            filename = Logic.HOLIDAY_FILE
            poll_dictionary = self.holiday_votes_dictionary
        elif self.season_button.isChecked():
            filename = Logic.SEASON_FILE
            poll_dictionary = self.season_votes_dictionary
        try:
            with open(filename, "w", newline='') as file:
                csv_writer = writer(file, delimiter=',')
                list_to_write = []
                for option, count in poll_dictionary.items():
                    if option != 'ballots':
                        list_to_write.append([option, count])
                    else:
                        for voter, vote in poll_dictionary[option].items():
                            list_to_write.append([voter, vote])
                print(list_to_write)
                csv_writer.writerows(list_to_write)
        except Exception as e:
            print(f"Error saving votes: {e}")

    def determine_outcome(self) -> str:
        """
        This checks the values of the keys in the appropriate dictionary and
        determines the outcome of the vote.
        :return: This returns a string that describes the outcome of the vote.
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
            if key != 'ballots':
                if votes > potential_winning_score:
                    potential_winner = key
                    potential_winning_score = votes
        for key, votes in poll_dictionary.items():
            if key != 'ballots':
                if votes == potential_winning_score:
                    ties_for_1st += 1
        if ties_for_1st > 1:
            outcome = 'Tie'
        else:
            outcome = potential_winner
        return outcome

    def results(self) -> None:
        """
        This function displays the votes each candidate, the votes they have
        have accrued, and the outcome of the vote so far to the user.
        :return: This returns nothing and may return None early if the user
        doesn't choose a poll.
        """
        outcome = self.determine_outcome()
        results_text = ''
        voter_text = 'VOTERS:\n'
        poll_dictionary = {}
        if self.holiday_button.isChecked():
            poll_dictionary = self.holiday_votes_dictionary
            self.exception_label.clear()
        elif self.season_button.isChecked():
            poll_dictionary = self.season_votes_dictionary
            self.exception_label.clear()
        else:
            return None
        if self.holiday_button.isChecked() or self.season_button.isChecked():
            for key, votes in poll_dictionary.items():
                if key == 'ballots':
                    # Separate each ballot on a new line
                    voter_text += '\n'.join([f'{voter}: {vote}' for voter, vote in votes.items()])
                else:
                    # Replace " votes" with an empty string
                    results_text += f'{key} has {votes}.\n'
            if outcome == 'Tie':
                results_text += "It's a tie!"
            else:
                results_text += f'{outcome} wins!'
        self.results_label.setText(results_text)
        self.voter_list.setText(voter_text)

        print("votes: ", poll_dictionary)
        self.user_input.setText('')
        self.user_input.setFocus()
        self.exception_label.setText("")

    def load_votes(self) -> None:
        """
        This loads the votes stored in files into the appropriate dictionary.
        """
        filename = "blank.txt"
        poll_dictionary = {}
        if self.holiday_button.isChecked():
            # filename = self.holiday_file
            poll_dictionary = self.holiday_votes_dictionary
        elif self.season_button.isChecked():
            # filename = self.season_file
            poll_dictionary = self.season_votes_dictionary
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line in file:
                        option, count = line.strip().split(":")
                        poll_dictionary[option] = int(count)
        except Exception as e:
            print(f"Error loading votes: {e}")


