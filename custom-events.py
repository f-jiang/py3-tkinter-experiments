from tkinter import Tk, Label, Button, StringVar

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_text = StringVar()
        self.label_text.set("This is our first GUI")
        self.label = Label(master, textvariable=self.label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.bind("<Enter>", self.surprise)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.bind("<Enter>", self.surprise)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    # http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
    # reference for tkinter event attributes
    def surprise(self, event):
        self.label_text.set("haHAA")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

