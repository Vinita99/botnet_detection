from tkinter import *
from tkinter import ttk
from tkinter import filedialog 

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Tkinter dialog widget")
        self.minsize(640,400)
        self.wm_iconbitmap('icon.ico')
        self.labelFrame=ttk.LabelFrame(self,text="open a file")
        self.labelFrame.grid(column=0,row=1,padx=20,pady=20)
        self.button()
    def button(self):
        self.button=ttk.Button(self.labelFrame,text="browse a file",command=self.fileDialog)
        self.button.grid(column=1,row=1)
    def fileDialog(self):
        self.filename=filedialog.askopenfilename(initialdir="/",title="select a file",filetype=(("jpeg","*jpg"),("all files","*.*")))

if __name__=='__main__':
    root=Root()
    root.mainloop()