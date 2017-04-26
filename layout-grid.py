from tkinter import Tk, Label, Button, W

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI")
        # sticky: align cell content N, S, E, W, NE, SW, etc.
        self.label.grid(row=1, column=1, rowspan=2, sticky=W)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1, column=2)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2, column=2)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

