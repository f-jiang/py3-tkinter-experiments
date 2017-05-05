from tkinter import Tk, Label, Button, Frame

class PageManager(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)

        self.pack(side='top', fill='both', expand=True)
        self.pages = {}

    def add_page(self, page):
        p = page(manager=self)
        p.grid(row=0, column=0, sticky='nsew')
        self.pages[page.__name__] = p

    def remove_page(self, page):
        del self.pages[page.__name__]

    def show_page(self, page):
        self.pages[page.__name__].tkraise()


class FirstPage(Frame):

    def __init__(self, manager):
        Frame.__init__(self, manager)

        label = Label(self, text='page 1')
        label.pack(side='top')
        button = Button(self, text='go to page 2', command=lambda: manager.show_page(SecondPage))
        button.pack()


class SecondPage(Frame):

    def __init__(self, manager):
        Frame.__init__(self, manager)

        label = Label(self, text='page 2')
        label.pack(side='top')
        button = Button(self, text='go to page 1', command=lambda: manager.show_page(FirstPage))
        button.pack()


if __name__ == '__main__':
    root = Tk()

    manager = PageManager(root)
    manager.add_page(FirstPage)
    manager.add_page(SecondPage)
    manager.show_page(FirstPage)

    root.mainloop()

