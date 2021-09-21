from files.file_reader import FileReader
from files.file_writer import FileWriter
from parsers.line_deletion_parser import LineDeletionParser
from parsers.universal_parser import UniversalParser


def run():
    file_path = input("Input file path to parse:")
    lines_to_delete = input("Input number of lines to delete or press enter to skip it:")

    file_reader = FileReader(file_path=file_path)
    line_deletion_parser = LineDeletionParser(int(lines_to_delete)) \
        if isinstance(lines_to_delete, int) else LineDeletionParser()
    file_writer = FileWriter(file_path=file_path)
    universal_parser = UniversalParser(file_reader, line_deletion_parser, file_writer)
    universal_parser.process_parser()


if __name__ == '__main__':
    run()
