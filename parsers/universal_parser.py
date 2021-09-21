DEFAULT_LINES_TO_DELETE_QUANTITY = 10


class UniversalParser:
    def __init__(self, file_reader, parser_processor, file_writer,
                 lines_to_delete_quantity=DEFAULT_LINES_TO_DELETE_QUANTITY):
        self.file_reader = file_reader
        self.parser_processor = parser_processor
        self.file_writer = file_writer
        self.lines_to_delete_quantity = lines_to_delete_quantity

    def process_parser(self):
        self.__read_books()
        lines_to_write = self.__parse_books()
        self.__write_books(lines_to_write)

    def __read_books(self):
        self.file_reader.read_lines()

    def __parse_books(self):
        self.parser_processor.set_list_of_lines(self.file_reader.list_of_read_lines)
        list_of_lines = self.parser_processor.run_parser()
        return list_of_lines

    def __write_books(self, lines_to_write):
        self.file_writer.write_lines(lines_to_write)
