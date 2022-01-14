import matplotlib.pyplot as plt

class Graph:
    def __init__(self, label1, label2, label3, value1, value2, value3, title):
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.title = title


label1 = input("Enter Graph Label 1: ")
label2 = input("Enter Graph Label 2: ")
label3 = input("Enter Graph Label 3: ")
value1 = input("Enter Graph Values 1: ")
value2 = input("Enter Graph Values 2: ")
value3 = input("Enter Graph Values 3: ")
title = input("Enter Graph Title: ")
g1 = Graph(label1, label2, label3, value1, value2, value3, title)
plt.title(str(g1.title))
plt.bar([g1.label1, g1.label2, g1.label3], [g1.value1, g1.value2, g1.value3])
plt.show()