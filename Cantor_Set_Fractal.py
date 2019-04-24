import turtle as t
t.pensize(5)
t.pencolor("blue")

def cantor(x,y,length):
  if(length>1):
    t.up()
    t.goto(x,y)
    t.down()
    t.forward(length)
    t.up()
    y=y-10
    t.goto(x,y)
    t.down()
    cantor(x,y,length/3)
    cantor(x+length*2/3,y,length/3)
    
cantor(-250,0,500)