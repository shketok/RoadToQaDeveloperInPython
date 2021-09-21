MAX_NUM_OF_LINES_TO_READ = 1000


class FileReader:
    def __init__(self, file_path, max_num_of_lines_to_read=MAX_NUM_OF_LINES_TO_READ):
        self.file_path = file_path
        self.max_num_of_lines_to_read = max_num_of_lines_to_read
        self.read_counter = 0
        self.list_of_read_lines = []

    def read_lines(self):
        with open(self.file_path) as file:
            while (line := file.readline().rstrip()) and (self.read_counter < self.max_num_of_lines_to_read):
                self.list_of_read_lines.append(line)
                self.read_counter += 1

        return self.list_of_read_lines


