ADDITIONAL_FILENAME = "_res."


class FileWriter:
    def __init__(self, file_path):
        file_path_parts = file_path.split(".")
        file_path = "".join(file_path_parts[0:-1] + [ADDITIONAL_FILENAME] + file_path_parts[-1:])
        self.file_path = file_path

    def write_lines(self, lines: list):
        with open(self.file_path, "w") as file:
            file.writelines("\n".join(lines))
