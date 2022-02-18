

class ConsoleGui:
    def __init__(self, header, text):
        self.header = header
        self.text = text


    def console_write(self):
        print(f"    < {self.header} >    ")
        print(f"{self.text}")
