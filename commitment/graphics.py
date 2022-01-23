from tkinter import *
from tkinter.ttk import *
import os

# solution from https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def app():
    root = Tk()
    root.geometry("500x750")
    center(root)
    root.title("Commitment")
    fp = open(os.path.expanduser('~') + '/.commitment/log.csv', 'r')
    log_list = fp.readlines()
    count = 0 
    for i in log_list:
        count += 1
    #label = Label(root, text =log_list).pack()
    canvas = Canvas(root)
    canvas.create_oval(10, 10, 80, 80, outline="#f11",
            fill="#1f1", width=2)
    canvas.pack()
    root.mainloop()