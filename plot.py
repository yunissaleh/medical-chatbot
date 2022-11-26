from tkinter import *
import pandas as pd
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def graph():
    column_names = ["id", "name", "temp", "hum", "blood", "noise", "loc", "day", "month", "year"]
    df = pd.read_csv("persons.csv", names=column_names)
    years = df.year.to_list()
    months = df.month.to_list()
    patients_addedByMonth = {}
    patients_addedByYear = {}

    for i in years:
        patients_addedByYear[i] = years.count(i)
    x1 = list(dict.fromkeys(years))
    y1 = list(patients_addedByYear.values())

    for i in months:
        patients_addedByMonth[i] = months.count(i)
    x2 = list(dict.fromkeys(months))
    y2 = list(patients_addedByMonth.values())

    grapw = Tk()
    grapw.title("plots")
    grapw.geometry("470x550")
    grapw.resizable(width=False, height=False)

    fig = Figure(figsize=(5,5),
                 dpi=110)

    canvas = FigureCanvasTkAgg(fig,
                               master=grapw)

    # create axes
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(224)
    # create the barchart
    ax1.bar(x1, y1)
    ax1.set_title('Patients added by year')
    ax1.set_ylabel('no. of patients')
    ax1.set_xlabel('year')

    ax2.bar(x2, y2)
    ax2.set_title('Patients added by month')
    ax2.set_ylabel('no of patients')
    ax2.set_xlabel('month')

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   grapw)

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


