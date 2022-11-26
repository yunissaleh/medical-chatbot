from tkinter import *
from plot import graph

from bot import respond, record_audio, there_exists
BG_GRAY = "#e6e6e6"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
MAX = 11
FONT = "Calibri 13"
FONT_BOLD = "Calibri 12 "
import time as time_
timestamp = int(time_.time())

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def second(self):
        def save_info():
            id_info = id.get()
            id_info = str(id_info)
            name_info = name.get()
            temp_info = temp.get()
            temp_info = str(temp_info)
            humidity_info = humidity.get()
            humidity_info = str(humidity_info)
            bp_info = bp.get()
            bp_info = str(bp_info)
            nl_info = nl.get()
            nl_info = str(nl_info)
            location_info = location.get()
            day_info = day.get()
            day_info = str(day_info)
            month_info = month.get()
            month_info = str(month_info)
            year_info = year.get()
            year_info = str(year_info)
            num_lines = sum(1 for line in open('persons.csv'))

            if num_lines < MAX:
                file = open("persons.csv", "a+")
                file.write(id_info)
                file.write(',')
                file.write(name_info)
                file.write(',')
                file.write(temp_info)
                file.write(',')
                file.write(humidity_info)
                file.write(',')
                file.write(bp_info)
                file.write(',')
                file.write(nl_info)
                file.write(',')
                file.write(location_info)
                file.write(',')
                file.write(day_info)
                file.write(',')
                file.write(month_info)
                file.write(',')
                file.write(year_info)
                file.write('\n')
                file.close()
                print(" User ", name_info, " has been registered successfully")

            if num_lines in range(MAX-10,MAX):
                err = Label(screen, text="      memory is almost full            ", bg="#ffcc00", fg=BG_COLOR)
                err.place(x=136, y=400)
            elif num_lines >= MAX:
                err = Label(screen, text="memory is full, can't add more patients", bg="#990000", fg=TEXT_COLOR)
                err.place(x=119, y=400)

            id_entry.delete(0, END)
            name_entry.delete(0, END)
            temp_entry.delete(0, END)
            humidity_entry.delete(0, END)
            bp_entry.delete(0, END)
            nl_entry.delete(0, END)
            location_entry.delete(0, END)
            day_entry.delete(0, END)
            month_entry.delete(0,END)
            year_entry.delete(0,END)


        screen = Toplevel(self.window)
        screen.geometry("470x550")
        screen.resizable(width=False, height=False)
        screen.configure(bg=BG_COLOR)
        screen.title("Patient Forum")
        heading = Label(screen, text="Patient Forum", bg=BG_COLOR, fg=TEXT_COLOR, width="500", height="3")
        heading.pack()
        line = Label(screen, width=10, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.098, relheight=0.004)
        id_text = Label(screen, text="ID * ", bg=BG_COLOR, fg=TEXT_COLOR)
        name_text = Label(screen, text="Name * ", bg=BG_COLOR, fg=TEXT_COLOR)
        temp_text = Label(screen, text="Temperature * ", bg=BG_COLOR, fg=TEXT_COLOR)
        humidity_text = Label(screen, text="Humidity *", bg=BG_COLOR, fg=TEXT_COLOR)
        bp_text = Label(screen, text="Blood Pressure *", bg=BG_COLOR, fg=TEXT_COLOR)
        nl_text = Label(screen, text="Noise Level *", bg=BG_COLOR, fg=TEXT_COLOR)
        location_text = Label(screen, text="Location *", bg=BG_COLOR, fg=TEXT_COLOR)
        day_text = Label(screen, text="Date *", bg=BG_COLOR, fg=TEXT_COLOR)

        id_text.place(x=35, y=70)
        name_text.place(x=35, y=140)
        temp_text.place(x=35, y=210)
        humidity_text.place(x=35, y=280)
        bp_text.place(x=250, y=70)
        nl_text.place(x=250, y=140)
        location_text.place(x=250, y=210)
        day_text.place(x=250, y=280)

        id = IntVar()
        name = StringVar()
        temp = IntVar()
        humidity = IntVar()
        bp = IntVar()
        nl = IntVar()
        location = StringVar()
        day = IntVar()
        month = IntVar()
        year = IntVar()


        id_entry = Entry(screen, textvariable=id, width="30")
        name_entry = Entry(screen, textvariable=name, width="30")
        temp_entry = Entry(screen, textvariable=temp, width="30")
        humidity_entry = Entry(screen, textvariable=humidity, width="30")
        bp_entry = Entry(screen, textvariable=bp, width="30")
        nl_entry = Entry(screen, textvariable=nl, width="30")
        location_entry = Entry(screen, textvariable=location, width="30")
        day_entry = Entry(screen, textvariable=day, width="5")
        month_entry = Entry(screen,textvariable=month,width="5")
        year_entry = Entry(screen,textvariable=year,width="16")


        id_entry.place(x=35, y=100)
        name_entry.place(x=35, y=170)
        temp_entry.place(x=35, y=240)
        humidity_entry.place(x=35, y=310)
        bp_entry.place(x=250, y=100)
        nl_entry.place(x=250, y=170)
        location_entry.place(x=250, y=240)
        day_entry.place(x=250, y=310)
        month_entry.place(x=290, y=310)
        year_entry.place(x=330, y=310)

        register = Button(screen, text="Register", width="25", height="2", command=save_info, bg="#29394b", fg=BG_GRAY,
                          activebackground="#4c698a",
                          activeforeground=BG_GRAY, borderwidth=0)
        register.place(x=135, y=360)

    glo = 0

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(bg=BG_COLOR)
        self.window.geometry("470x550")

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="VIRTUAL ASSISTANT", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.078, relheight=0.018)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=1)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.63, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=5, bg="#29394b", fg=BG_GRAY,
                             activebackground="#4c698a",
                             activeforeground=BG_GRAY, borderwidth=0, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.65, rely=0.008, relheight=0.03, relwidth=0.11)

        voice_button = Button(bottom_label, text="Talk", font=FONT_BOLD, width=5, bg="#29394b", fg=BG_GRAY,
                              activebackground="#4c698a",
                              activeforeground=BG_GRAY, borderwidth=0,
                              command=lambda: self._on_enter_talk(None))
        voice_button.place(relx=0.65, y=48, relheight=0.028, relwidth=0.11)

        self.plot_button = Button(bottom_label, text="Plot", font=FONT_BOLD, width=5, bg="#29394b", fg=BG_GRAY,
                                                     activebackground="#4c698a",
                                                     activeforeground=BG_GRAY, borderwidth=0,
                                                     command=lambda: graph())
        self.plot_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.10)

        register_button = Button(bottom_label, text="Add", font=FONT_BOLD, width=5, bg="#29394b", fg=BG_GRAY,
                                 activebackground="#4c698a",
                                 activeforeground=BG_GRAY, borderwidth=0, command=lambda: self.second())
        register_button.place(relx=0.88, rely=0.008, relheight=0.06, relwidth=0.10)


    def _on_enter_pressed(self, event):
        global glo
        msg = self.msg_entry.get()
        if there_exists(["plot","plotting","graph"],msg):
            self.plot_button.invoke()
        self._insert_message(msg, "You")

    def _on_enter_talk(self, event):
        msg = record_audio()
        if there_exists(["plot","plotting","graph"],msg):
            self.plot_button.invoke()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL, )
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED, )

        msg2 = f"Sandy:{respond(msg.lower())}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
    endt = int(time_.time()) - timestamp
    print("Process time: ", endt, " seconds")