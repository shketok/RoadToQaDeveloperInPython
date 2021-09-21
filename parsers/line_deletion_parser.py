from random import randint

LINES_TO_DELETE = 5


class LineDeletionParser:

    def __init__(self, lines_to_delete=LINES_TO_DELETE):
        self.list_of_lines = None
        self.lines_to_delete = lines_to_delete

    def set_list_of_lines(self, list_of_lines):
        self.list_of_lines = list_of_lines

    def run_parser(self) -> list:
        if len(self.list_of_lines) - 1 < self.lines_to_delete:
            raise Exception("Size of list is less than lines to delete quantity")

        for i in range(0, self.lines_to_delete):
            self.list_of_lines.pop(randint(1, len(self.list_of_lines)))  # ignoring first line

        return self.list_of_lines
