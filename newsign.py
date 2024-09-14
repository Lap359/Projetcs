from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter.messagebox import *

root=Tk()
root.geometry('550x400')
root.title('Signup window')

#Please improve this:
def not_implemented_yet():
    showinfo(title='Feature not implemented yet!',message='Are you a developer? Please improve this program.')

laebl=Label(root,text="Subject Name:").place(x=50,y=100)
eetry=Entry(root,width=40).place(x=170,y=100)
laeblage=Label(root,text="Subject Age:").place(x=50,y=130)
eetryage=Entry(root,width=40).place(x=170,y=130)
laeblemail=Label(root,text="Subject E-Mail:").place(x=50,y=160)
eetryemail=Entry(root,width=40).place(x=170,y=160)
laebltown=Label(root,text="Subject Hometown:").place(x=50,y=190)
eetrytown=Entry(root,width=40).place(x=170,y=190)
signup_btn=Button(root,text='Sign Me Up!',command=not_implemented_yet).place(x=135,y=260)

laebltown=Label(root,text="Subject Locale:").place(x=50,y=220)
var=StringVar
dropdowns=Combobox(root,width=37,textvariable=var)
dropdowns['value']=('Vietnamese', 'US', 'UK', 'Russian', 'Privacy')
dropdowns.place(x=170, y=220)
dropdowns.current(4)

# treelist=Treeview(root)
# treelist.insert('',END,text='bruhh')
# treelist.place(x=220, y=60)

# img=Image.open("windows-xp-bliss-4k-lu-1920x1080.jpg")
# img_resize=img.resize((1024,576))
# photonian=ImageTk.PhotoImage(img_resize)
# llble=Label(image=photonian)
# llble.pack()

root.mainloop()