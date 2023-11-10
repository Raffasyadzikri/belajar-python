from turtle import*

getscreen()
bgcolor("Red")

pencolor("blue")
pensize(1)
shape("Turtle")

speed(1)

init_size = 30
init_angle = 90

for i in range(36):
    for i in range(3):
        forward(100)
        left(120)
        init_size +=10
        left(7)

done()