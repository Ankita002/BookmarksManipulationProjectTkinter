import codecs
from tkinter import *
 
from tkinter import ttk
import tkinter as tk

import webbrowser
 
    



def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
f = codecs.open("YOUR_URL")
text=f.read()
 

 

 
def GetListOfSubstrings(stringSubject,string1,string2):
    MyList = []
    intstart=0
    strlength=len(stringSubject)
    continueloop = 1

    while(intstart < strlength and continueloop == 1):
        intindex1=stringSubject.find(string1,intstart)
        if(intindex1 != -1): #The substring was found, lets proceed
            intindex1 = intindex1+len(string1)
            intindex2 = stringSubject.find(string2,intindex1)
            if(intindex2 != -1):
                subsequence=stringSubject[intindex1:intindex2]
                MyList.append(subsequence)
                intstart=intindex2+len(string2)
            else:
                continueloop=0
        else:
            continueloop=0
    return MyList 
def link(ar):
    webbrowser.open_new(ar)

l1=GetListOfSubstrings(text,'">','</A>')
l2=GetListOfSubstrings(text,'<DT><A HREF="','"')

 

d={}
for i in range(1,len(l1)):
    d[l1[i]]=l2[i]


root = Tk()
 
root.title = 'Bookmark Application'
root.geometry('1200x1000')
main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)
canvas=Canvas(main_frame)
canvas.pack(side=LEFT,fill=BOTH,expand=1)
my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview)

my_scrollbar.pack(side=RIGHT,fill=Y)

canvas.configure(yscrollcommand=my_scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
second_frame=Frame(canvas)
canvas.create_window((0,0),window=second_frame,anchor="nw")
 
j=0
for i in d.keys():

    ttk.Button(second_frame, text=i, command= lambda i=i: link(d[i])).grid(row=j,column=0)
    j=j+1
    

   
 

root.mainloop()
