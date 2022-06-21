import tkinter as tk
import tkinter.messagebox as tkm
root =tk.Tk()
root.title("a")
root.geometry("300x500")
font="Time New Roman"
font1=""

entry = tk.Entry(justify = "right", width = 11, font = ('Times New Roman', 40))
entry.grid(row = 0, columnspan = 10)

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)

def equal(event):
    fm=entry.get()
    entry.delete(0, tk.END)
    ans= eval(fm)
    entry.insert(tk.END, ans)

a=0
list=[[4,0],[3,0],[3,1],[3,2],[2,0],[2,1],[2,2],[1,0],[1,1],[1,2]]
for i,j in list:
    button=tk.Button(root,text=a,font=(font,30),command=button_click,width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=i,column=j)
    a+=1

buttonequal = tk.Button(root,text='=',font=(font,30),command= equal,width = 4, height = 2)
buttonequal.bind("<1>", equal)
buttonequal.grid(row = 4,column = 2,padx=4,pady = 2)

buttonequal = tk.Button(root,text='+',font=(font,30),command=button_click,width = 4, height = 2)
buttonequal.bind("<1>", )
buttonequal.grid(row = 4,column = 1,padx=4,pady = 2)

dis=tk.Entry(root,font=(font,40), justify="center")
dis.pack
root.mainloop()