import plot
import consolegui

#YusufPlot b1

'''
plots example:
g1 = plot.Plot((3,4,5), (4,9,4), "hello")
g1.plot_graph()
'''

consolegui.ConsoleGui("Welcome To YusufPlot!", "Welcome to YusufPlot, maintained and made by github.com/fatycaty").console_write()

consolegui.ConsoleGui("Create Plot", "Enter an array (example: 'x,y,z') which will represent the X").console_write()
plot_x_1_inp = input(" First value >  ")
plot_x_2_inp = input(" Second value >  ")
plot_x_3_inp = input(" Third value >  ")

consolegui.ConsoleGui("Create Plot", "Enter an array (example: 'x,y,z') which will represent the Y").console_write()
plot_y_1_inp = input(" First value >  ")
plot_y_2_inp = input(" Second value >  ")
plot_y_3_inp = input(" Third value >  ")

consolegui.ConsoleGui("Create Plot", "Enter a title for your plot").console_write()
plot_title_input = input(" Title >  ")

plot_x = (plot_x_1_inp, plot_x_2_inp, plot_x_3_inp)
plot_y = (plot_y_1_inp, plot_y_2_inp, plot_y_3_inp)

p1 = plot.Plot(plot_x, plot_y, plot_title_input)
p1.plot_graph()

print(plot)
