
class TerminalService:
    """A service that handles terminal operations.

    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def read_text(self, prompt):

        return input(prompt)

    def read_number(self, prompt):

        return float(input(prompt))

    def write_text(self, text):

        print(text)
