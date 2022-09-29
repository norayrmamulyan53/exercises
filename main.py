from helper.exceptions import IncludesStringError


def file_includes_string(file_path, string=""):
    """
    Opens the specified file by path and checks if the specified
    string is found in the contents of this file.

    Args:
        file_path: Path to the file to check
        string: The string to be found in the specified file
    """
    try:
        with open(file_path, "r") as file:
            if string in file.read():
                raise IncludesStringError
        print(f"In the \"{file_path}\" string \"{string}\" doesn't exists")
    except IncludesStringError:
        print(f"\"{string}\" is found in \"{file_path}\" file")
    except FileNotFoundError:
        print(f"File with path \"{file_path}\" is not found")


class Parent:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        return self.name


class Child(Parent):
    def __init__(self, age, name):
        super().__init__(name)
        pass


bla = Child(23, "hehe")
print(bla.print_name())
