import colorama
import os

class ConsoleGui:
    def __init__(self, header, text):
        self.header = header
        self.text = text


    def console_write(self):
        print(colorama.Fore.CYAN + "<| " + self.header + " |>")
        print(colorama.Fore.BLUE + self.text)
    

def console_clear_text():
        if os.name == "nt" or "dos":
            os.system("cls")
        else:
            os.system("clear")
