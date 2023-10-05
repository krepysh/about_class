import turtle 

def dottedline(t, length):
    for i in range(4):
        t.fd(length)
        t.up()
        t.fd(length)
        t.down()

bob = turtle.Turtle()
dottedline(bob, 100)
turtle.mainloop()

