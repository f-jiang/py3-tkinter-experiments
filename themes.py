from Tkinter import *
from ttk import *

class App():
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    master.title("Just my example")
    self.label = Label(frame, text="Type very long text:")

    self.entry = Entry(frame)

    self.button = Button(frame,
                         text="Quit", width=15,
                         command=frame.quit)


    self.slogan = Button(frame,
                         text="Hello", width=15,
                         command=self.write_slogan)

    self.label.grid(row=0, column=0)
    self.entry.grid(row=0, column=1)
    self.slogan.grid(row=1, column=0, sticky='e')
    self.button.grid(row=1, column=1, sticky='e')

  def write_slogan(self):
    print("Tkinter is easy to use!")

root = Tk()
root.style = Style()
#('clam', 'alt', 'default', 'classic')
root.style.theme_use("clam")

app = App(root)
root.mainloop()

