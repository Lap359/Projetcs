from tkinter import *
from tkinter import ttk
from tkinter import filedialog

windowroot=Tk()
windowroot.title('Text Editor')
windowroot.geometry('600x400')
menubar=Menu()
types=[
    ('Plain Text','*.txt'),
    ('All Types','*.*')
]
def openfile():
    filename=filedialog.askopenfilename(title='Open',filetypes=types)
    with open(filename,'r+') as file:
        content=file.read()
        textarea.delete('1.0',END)
        textarea.insert('1.0',content)
def savefile():
    filesave=filedialog.asksaveasfilename(filetypes=types,title='Save')
    contents=str(textarea.get('1.0',END))
    file=open(filesave,'+a')
    file.write(contents)
menu_file=Menu(menubar)
menu_file.add_command(
    label='Open',
    command=openfile
)
menu_file.add_command(
    label='Save',
    command=savefile
)
scroll=Scrollbar(windowroot)
scroll.pack(side=RIGHT,fill=Y)
textarea=Text(master=windowroot,yscrollcommand=scroll.set)
textarea.pack(fill=BOTH)
menubar.add_cascade(menu=menu_file,label='Main')
scroll.config(command=textarea.yview)
windowroot.config(menu=menubar)

mainloop()