from tkinter import*
from PIL import ImageTk,Image 

root=Tk()
root.title("Working on Canvas Using Functions")
root.geometry("600x600")
img=ImageTk.PhotoImage(Image.open("start.png"))
canvas=Canvas(root,width=590,height=510,bg="white",highlightbackground="lightgray")
oldx=50
oldy=50
newx=50
newy=50
direction=""
def right_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    global direction
    oldx=newx 
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
    
    
def left_dir(event):
    global oldx 
    global oldy 
    global newx
    global newy
    global direction
    oldx=newx
    oldy=newy
    newx=newx-5
    direction="left"
    draw(direction,oldx,oldy,newx,newy)
def down_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    global direction 
    oldx=newx
    oldy=newy
    newy=newy+5
    direction="down"
    draw(direction,oldx,oldy,newx,newy)
    
def up_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    global direction 
    oldx=newx
    oldy=newy
    newy=newy-5
    direction="up"
    draw(direction,oldx,oldy,newx,newy)
    
  
    
canvas.pack()
myimage=canvas.create_image(50,50,image=img)
label1=Label(root,text="enter a color:")
label1.place(relx=0.6,rely=0.9,anchor=CENTER)
input1=Entry(root)
input1.place(relx=0.8,rely=0.9,anchor=CENTER)
input1.insert(0,"black")

def draw(direction,oldx,oldy,newx,newy):
    fillcolor=input1.get()
    if direction=="right":
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolor)
        canvas.move(myimage,5,0)
    if direction=="left":
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolor)
        canvas.move(myimage,-5,0)
    if direction=="down":
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolor)
        canvas.move(myimage,0,5)
    if direction=="up":
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fillcolor)
        canvas.move(myimage,0,-5)
        
    
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Down>",down_dir)
root.bind("<Up>",up_dir)

    
root.mainloop()
