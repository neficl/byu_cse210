from game.terminal_service import TerminalService
from game.display import Display
from game.puzzle import List


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        display (Display): The display of the jumper.
        is_playing (boolean): Whether or not to keep playing.
        word (List): the word from a list of words.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._display = Display()
        self._is_playing = True
        self._list = List()
        self._terminal_service = TerminalService()
        self.random_word = self._list.random_word()
        self.letter_guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        self._terminal_service.write_text(
            self._display.display_word(str(self.random_word)))

        self._terminal_service.write_text(self._display.display_parachute())

        while self._is_playing:
            self._get_inputs()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self.letter_guess = self._terminal_service.read_text(
            "\nGuess a letter: ")

    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(
            self._display.display_word(self.random_word, self.letter_guess))
        self._terminal_service.write_text(self._display.display_parachute())
        if self._display._is_dead():
            self._is_playing = False
        if self._display._winner():
            self._is_playing = False
