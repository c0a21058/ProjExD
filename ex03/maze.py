import tkinter as tk
import maze_maker


key=""
cx,cy=150,150
mx,my=1,1

def key_down(event):
    global key
    key = event.keysym                                                   

def key_up(event):
    global key
    key=""   

def main_proc():                                                         
    global cx, cy, key, tori, mx, my                                     
    if key == 'Up'  and  maze_list[my-1][mx] == 0:                         
        cy -= 100                                                        
        my -= 1                                                          
        
    elif key == 'Down'  and  maze_list[my+1][mx] == 0:                    
        cy += 100                                                      
        my += 1                                                         

    elif key == 'Right' and  maze_list[my][mx+1] == 0:                   
        cx += 100                                                        
        mx += 1                                                          

    elif key == 'Left'  and  maze_list[my][mx-1] == 0:                    
        cx -= 100                                                        
        mx -= 1                                                          
    maze.after(100,main_proc)    
    canvas.coords("tori", cx, cy)                                                                                                           
                                               
def kusodori():                                                          
    global tori, cx, cy                                             
    tori=tk.PhotoImage(file="ex03/fig/7.png")
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
kusodori()

maze.mainloop()