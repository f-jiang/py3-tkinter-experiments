from tkinter import Tk, Label, Button
from multiprocessing import Process
from time import sleep

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

def gui_loop():
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()

def backend_loop():
    c = 0
    while True:
        print(c)
        c += 1
        sleep(1)

if __name__ == "__main__":
    Process(target=gui_loop).start()
    Process(target=backend_loop).start()

