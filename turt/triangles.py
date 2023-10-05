import turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def nangle(t, n, length):
    for i in range(n):
        polygon(t, n, length)
        t.lt(360 / n)

def change_color_each_pulygon(t, n, length):
    for i in range(n):
        t.color("red")
        polygon(t, n, length)
        t.color("blue")
        t.lt(360 / n)

def main():
    bob = turtle.Turtle()
    bob.speed(0)
    bob.hideturtle()
    change_color_each_pulygon(bob, 10, 50)
    turtle.mainloop()

if __name__ == "__main__":
    main()