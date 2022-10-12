
class Display:
    """Displays the word to guess and the parachute. 

    The responsibility of Display is to check the guess against the word and update the display to reflect the changes. 

    Attributes:
        _given_word (List[char]): The word to be guessed.
        _length (int): Length of the word to be guessed.
        _letter_guess (Boolean): Boolean if the guessed letter is in the give_word.
        _lines_to_letter (List[char]): The characters to be displayed.
        _lines_to_letter_string (string): The string to return to the director.
        _parachute (List[string]): Contains the parachute to be displayed.
        _p_index (List[int]): A list of all the indexes of characters to remove on the parachute.
    """

    def __init__(self):
        """Constructs a new Display.

        Args:
            self (Display): An instance of Display.
        """
        self._given_word = []
        self._length = 0
        self._letter_guess = True
        self._lines_to_letter = []
        self._lines_to_letter_string = ""
        self._parachute = ["  ", "___", "\n", " ", "/", "___", "\\", "\n", " ", "\\", "   ",
                           "/", "\n", "  ", "\\", " ", "/", "\n", "   ", "o", "\n  /|\\\n  / \\\n\n^^^^^^^"]
        self._p_index = [1, 4, 6, 5, 9, 11, 14, 16]
        self._parachute_string = ""

    def display_word(self, word, letter=""):
        """ This method will build the word to guess

        The responsibility of display_word is to build the word using "_" where a letter has not been guessed
        It will then replace the "_" with the letter correctly guessed

        Parameters:
            self (Display):
            word (string): The word being guessed.
            letter (char): The letter being guessed.

        Returns:
            _lines_to_letters_string (string): the string built to display the word.
        """
        self._lines_to_letter_string = ""
        # Only runs once for the first round before a guess is made
        if letter == "":
            self._length = len(word)
            for item in word:
                self._given_word.append(item)

            for x in range(self._length):
                self._lines_to_letter.append("_")
        # Every round after the initializion
        else:
            self._letter_guess = False
            for item in self._given_word:
                if item == letter:
                    self._lines_to_letter[self._given_word.index(
                        item)] = letter
                    self._letter_guess = True

        # Prints out the word with spaces, "_", and correctly guessed letters
        for item in self._lines_to_letter:
            self._lines_to_letter_string += (item + " ")
        self._lines_to_letter_string += "\n"
        return self._lines_to_letter_string

    def display_parachute(self):
        """ This method will build the parachute

        The responsibility of display_parachute is to build the parachute
        It will then replace the parts of the parachute with empty spaces " " when a guess is incorrect.
        Once the user runs out of guesses, it will return a false to change the state of the game.

        Parameters:
            self (Display):
        Returns:
            _parachute_string (string): the string built to display the parachute.
        """
        self._parachute_string = ""
        # If they guessed correctly, no change to the parachute
        if self._letter_guess:
            for item in self._parachute:
                print(item, end="")
            return self._parachute_string
        # Remove part of parachute and replace with a " "
        else:
            if self._p_index[0] <= 16:
                self._parachute.pop(self._p_index[0])
                self._parachute.insert(self._p_index[0], " ")

            # The last round will also change the head into an "x"
            if (self._p_index[0] == 16):
                self._parachute.pop(19)
                self._parachute.insert(19, "x")
            self._p_index.pop(0)

            for item in self._parachute:
                self._parachute_string += item
            self._parachute_string += "\n"

            return self._parachute_string

    def _is_dead(self):

        return (self._parachute[19] == "x")

    def _winner(self):

        return (self._given_word == self._lines_to_letter)
