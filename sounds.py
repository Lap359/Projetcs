# #The playsound library:
# from playsound import *
# playsound('assets/y2mate.com - Ghost  Mary On A Cross Official Audio.mp3')

# from pydub import *
# from pydub.playback import play
# sung=AudioSegment.from_wav('assets/y2mate.com - Ghost  Mary On A Cross Official Audio.wav')
# play(sung)

from tkinter import *
from winsound import *
from tkinter import ttk
root=Tk()
root.title('Program')
frm=ttk.Frame(root)
frm.grid()
file=StringVar()
file_entry=ttk.Entry(frm,width=10,textvariable=file)
file_entry.grid(column=5,row=0)
play=ttk.Button(frm,text='Play!',command=PlaySound('file',SND_FILENAME))
play.grid(column=5,row=1)
root.mainloop()

# import os
# file='assets/"y2mate.com - Ghost  Mary On A Cross Official Audio.mp3"'
# os.system('mpg123 ' + file)
