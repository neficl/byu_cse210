import random


class List:
    """Contains a list of words that will be chosen at random. 

    The responsibility of List is to generate a random word.

    Attributes:
        _list (List[str]): list of words to be chosen at random.
        _word (str): The chosen word from the list.
    """

    def __init__(self):
        """Constructs a new List of words.

        Args:
            self (List): An instance of list.
        """
        self._list = ["star", "beach", "countryside",
                      "meadow", "forest", "canopy", "flower"]
        self._word = ""
        self.random_word()

    def random_word(self):
        """Selects a random word from the list

        Args:
            self (List): An instance of List.

        Returns:
            string: Word from the list"""
        random_index = random.randint(0, 6)
        return self._list[random_index]
