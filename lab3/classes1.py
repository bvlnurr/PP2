class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter string: ")

    def printString(self):
        print(self.s.upper())
