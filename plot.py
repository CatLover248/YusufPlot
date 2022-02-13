import matplotlib.pyplot as plt


class Plot:
    def __init__(self, x, y, title):
        self.x = x
        self.y = y
        self.title = title

    def plot_graph(self):
        plt.title(self.title)
        plt.plot(self.x, self.y)
        plt.show()

