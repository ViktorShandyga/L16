class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name

    def display_greeting(self):
        print(f"Hello! I am {self.name}, one of the best programming languages!")

class Python(ProgrammingLanguage):
    def __init__(self):
        super().__init__("Python")

class Java(ProgrammingLanguage):
    def __init__(self):
        super().__init__("Java")
class CPlusPlus(ProgrammingLanguage):
    def __init__(self):
        super().__init__("C++")
if __name__ == "__main__":
    python = Python()
    java = Java()
    cpp = CPlusPlus()

    python.display_greeting()
    java.display_greeting()
    cpp.display_greeting()
