import tkinter as tk
import maze_maker
import random


key=""
cx,cy=150,150#こうかとんの初期座標
mx,my=1,1
tmr=0
j=None
koukaton="ex03/fig/7.png"
yakitori="ex03/yakitori.png"
def count_up():#タイムをカウントする関数
    global tmr,mx,my,goal_x,goal_y,j
    tmr=tmr+1
    label["text"]=tmr
    j=maze.after(1000,count_up)
    if tmr>=8:
        restart() 
 

def startgoal():  #スタートとゴールを決める関数                                                                            
    global goal_x, goal_y                                                
    while True:                                                          
        goal_x = random.randint(12,14)                                   
        goal_y = random.randint(5,8)                                    
        if maze_list[goal_y][goal_x] == 0:                              
            break                                                        
    canvas.create_rectangle(100,100,200,200,fill = "black")  #スタート地点を黒にする             
    canvas.create_rectangle(goal_x*100,goal_y*100,(goal_x*100)+100,#ゴールを赤くする
    (goal_y*100)+100,fill = "red")

def key_down(event):
    global key
    key = event.keysym                                                   

def key_up(event):
    global key
    key=""   

def main_proc():     #こうかとんの座標の計算をする関数                                               
    global cx, cy, key, tori, mx, my,goal_x,goal_y ,j                         
    if key == 'Up'  and  maze_list[my-1][mx] == 0:   #↑を押した時の処理                 
        cy -= 100                                                        
        my -= 1                                                          
        
    elif key == 'Down'  and  maze_list[my+1][mx] == 0: #↓を押した時の処理             
        cy += 100                                                      
        my += 1                                                         

    elif key == 'Right' and  maze_list[my][mx+1] == 0:  #→を押した時の処理            
        cx += 100                                                        
        mx += 1                                                          

    elif key == 'Left'  and  maze_list[my][mx-1] == 0:  #←を押した時の処理       
        cx -= 100                                                        
        mx -= 1                                                              
    canvas.coords("tori", cx, cy)  
    if  my == goal_y and  mx == goal_x:    
        pass                                                           
    else:                                                                
        maze.after(100,main_proc)
    fin()

def restart():#タイム、こうかとんの座標を初期化する
    global cx,cy,tmr,mx,my
    cx,cy=150,150
    mx,my=1,1
    tmr=0

def fin(): #ゴールした時の表記をする関数                                                     
    global jid,mx,my,goal_x,goal_y ,koukaton,yakitori                                                      
    if my== goal_y and mx == goal_x:
        koukaton=yakitori
        kusodori()
        message = tk.Message(maze, text="焼き鳥",font = ("",40),
        bg = "yellow",fg = "red")
        message.pack()                                
        maze.after_cancel(j)                                             


def kusodori():   #こうかとんを呼び出す関数                                          
    global tori, cx, cy,koukaton                                      
    tori=tk.PhotoImage(file=koukaton)
    canvas.create_image(cx,cy,image=tori,tag="tori")

maze=tk.Tk()
maze.geometry("1500x900")
maze.title = ("迷えるこうかとん") 

canvas = tk.Canvas(maze, width = 1500,
                   height = 900,bg = 'black')   
canvas.place(x=0, y=0)
maze.bind("<KeyPress>",key_down)                                       
maze.bind("<KeyRelease>",key_up) 
maze.after(100,main_proc) 
maze_list=maze_maker.make_maze(15,9) 
maze_maker.show_maze(canvas, maze_list)
startgoal()
kusodori()
label=tk.Label(maze,font=("Times New Roman",60))
label.pack()
count_up()
maze.mainloop()
