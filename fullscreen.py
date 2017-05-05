from tkinter import Tk, Label, Button

root = Tk()

quit_btn = Button(root, text="quit", command=root.quit)
quit_btn.pack()

# maximize window
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(w, h))

# fullscreen mode - hide menu bar, system tray, etc.
root.overrideredirect(1)

root.mainloop()
