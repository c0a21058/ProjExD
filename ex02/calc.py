import tkinter as tk
import tkinter.messagebox as tkm

root =tk.Tk()
root.title("a")
font=("Time New Roman",30)


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

def hanten(event):
    fm=entry.get()
    entry.delete(0, tk.END)
    ans= int(fm)*-1
    entry.insert(tk.END, ans)

def dl(event):
    entry.delete(0,tk.END)

def dl_1(event):
    i=entry.get()
    entry.delete(len(i)-1,tk.END)

def cat_age(event):
    old=entry.get()
    old=int(old)
    ans=0
    entry.delete(0,tk.END)
    if old==0:
        ans=0
    elif 1<=old<2:
        ans=20
    elif old<0:
        ans="?"
    else:
        ans=20+4*(old-1)
    entry.insert(tk.END, ans)



def kaizyo(event):
    ans=1
    fm=entry.get()
    entry.delete(0,tk.END)
    for i in range(int(fm)):
        ans*=(i+1)
    entry.insert(tk.END, ans)
    

a=0
list=[[5,1],[4,0],[4,1],
      [4,2],[3,0],[3,1],
      [3,2],[2,0],[2,1],
      [2,2]]
for i,j in list:
    button=tk.Button(root,text=a,font=font,width=4,height=1,bg="black",fg="white")
    button.bind("<1>",button_click)
    button.grid(row=i,column=j)
    a+=1

buttonequal = tk.Button(root,text='=',font=font,width = 4, height = 1,bg="black",fg="white")
buttonequal.bind("<1>", equal)
buttonequal.grid(row = 5,column = 2)

buttonequal = tk.Button(root,text='+-',font=font,width = 4, height = 1,bg="black",fg="white")
buttonequal.bind("<1>", hanten)
buttonequal.grid(row = 5,column = 0)

buttonequal = tk.Button(root,text='!',font=font,width = 4, height = 1,bg="black",fg="white")
buttonequal.bind("<1>", kaizyo)
buttonequal.grid(row = 1,column = 1)

buttonequal = tk.Button(root,text='AC',font=font,width = 4, height = 1,bg="black",fg="white")
buttonequal.bind("<1>", dl)
buttonequal.grid(row = 1,column = 3)

buttonequal = tk.Button(root,text='C',font=font,width = 4, height = 1,bg="black",fg="white")
buttonequal.bind("<1>", dl_1)
buttonequal.grid(row = 1,column = 2)

buttonequal = tk.Button(root,text='猫',font=font,width = 4, height = 1,bg="black",fg="white")
buttonequal.bind("<1>", cat_age)
buttonequal.grid(row = 1,column = 0)

symbols=["+","-","/","*"]
n=2
for i in symbols:
    buttonsymbol = tk.Button(root,text=i,font=font,width = 4, height = 1,bg="black",fg="white")
    buttonsymbol.bind("<1>", button_click)
    buttonsymbol.grid(row=n,column=3)
    n+=1

dis=tk.Entry(root,font=(font,40), justify="center")
dis.pack
root.mainloop()