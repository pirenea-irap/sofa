# -*- coding: utf-8 -*-
"""Detect peaks in data based on their amplitude and other features."""

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

import numpy as np


x = np.arange(0, 5, 0.1)
y = np.sin(x)
print(x, type(x))

figure = Figure(dpi=100)
canvas = Canvas(figure)
ax = figure.add_subplot(111)
ax.hold(False)

ax.set_title("titi")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")

mask = [x > 4.0]
xx = x[mask]
yy = y[mask]
ax.hold(True)
ax.plot(x, y)
ax.plot(xx, yy)
# print("OUT self.plot.lines", self.ax.lines)
# self.ax.set_title(title)
# self.ax.set_xlabel(xlabel)
# self.ax.set_ylabel(ylabel)
# [x1, x2, y1, y2] = self.ax.axis()
# if min_x < 0.0:
#     min_x = x1
# if max_x < 0.0:
#     max_x = x2
# self.ax.axis([min_x, max_x, y1, y2])
# self.ax.hold(hold)
# test annotations
# x = x[ind]
# y = y[ind]
# for i, j in zip(x, y):
# ax.annotate(str(j), xy=(i, j))
#     self.ax.annotate("{:.3f}".format(float(j)), xy=(i, j), size=10)
# self.draw()
#
# plt.plot(x, y)
ax.show()
