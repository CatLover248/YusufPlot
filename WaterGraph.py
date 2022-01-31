#MIT License

#Copyright (c) 2022 Yusuf

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.




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
plt.bar([g1.label1, g1.label2, g1.label3], [g1.value1, g1.value2, g1.value3], align="center")
plt.show()
