
# diaplays the contents of the notepad files in terminal 
from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
  
root = Tk() 
root.geometry('200x100') 
  
# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('any files', '*.*')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
  
btn = Button(root, text ='Open', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 
  
mainloop() 