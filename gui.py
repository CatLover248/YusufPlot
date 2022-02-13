#imports
from tkinter import *

import plot


def create_onbuttonpress(x,y):
    print("Create button has been pressed")
    g1 = plot.Plot(x,y, "title")
    g1.plot_graph()


def window():

    MainWindow = Tk()

    MainWindow.title("YusufPlot b1-dev")
    MainWindow.geometry("600x600")

    logo = Label(MainWindow, text="YusufPlot", font=("BOLD", 50))
    logo.pack()

    # - - x - -

    x_txt1 = Label(text="X")
    x_txt1.pack()

    x_tb1 = Text(MainWindow,bg="gray", height=1, width=15)
    x_tb1.pack()


    x_tb2 = Text(MainWindow,bg="gray", height=1, width=15)
    x_tb2.pack()


    x_tb3 = Text(MainWindow,bg="gray", height=1, width=15)
    x_tb3.pack()

    # - - y - -

    y_txt1 = Label(text="Y")
    y_txt1.pack()

    y_tb1 = Text(MainWindow, bg="gray", height=1, width=15)
    y_tb1.pack()

    y_tb2 = Text(MainWindow, bg="gray", height=1, width=15)
    y_tb2.pack()

    y_tb3 = Text(MainWindow, bg="gray", height=1, width=15)
    y_tb3.pack()

    # - - title - -

    title_txt1 = Label(text="Title")
    title_txt1.pack()

    title_tb1 = Text(MainWindow, bg="gray", height=1, width=15)
    title_tb1.pack()

    # - - create - -

    create_button = Button(text="Create", width=8, height=1, bg="gray", command=lambda: create_onbuttonpress((x_tb1.get(1.0, "end-1c"), x_tb2.get(1.0, "end-1c"), x_tb3.get(1.0, "end-1c")), (y_tb1.get(1.0, "end-1c"), y_tb2.get(1.0, "end-1c"), y_tb3.get(1.0, "end-1c"))))
    create_button.pack()

    #Main window loop
    MainWindow.mainloop()