from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

def buildCanvas(figure, master):
    canvas = FigureCanvasTkAgg(figure, master)
    canvas.show()
    canvas.get_tk_widget().grid(row=0, column=0)
    return canvas
