import turtle
from random import choice,randint # для шарика
from playsound import playsound # для музыки

playsound('ping.mp3', False)

# создаём площадку - стол
okno = turtle.Screen()
okno.title("Ping-Pong")
okno.setup(width=1.0,height=1.0) # устанавливаем на весь экран
okno.bgcolor("lightyellow")
okno.tracer(1) # регулируем скорость мячика

# создаём границу для ограничения игровой площадки
granica = turtle.Turtle()
granica.speed(0) # делаем быстрее отрисовку
granica.color('palegreen')
granica.begin_fill() # добавляем для заливки поля
granica.goto(-500,300)
granica.goto(500,300)
granica.goto(500,-300)
granica.goto(-500,-300)
granica.goto(-500,300)
granica.penup()
granica.end_fill()

# рисуем линию посередине поля
granica.goto(0,300)
granica.color('honeydew')
granica.width(10)
granica.setheading(270) # для того чтобы линия рисовалась вниз
for i in range(25):
    if i%2==0:
        granica.forward(24)
    else:
        granica.up()
        granica.forward(24)
        granica.down()
        granica.hideturtle()

# создаём ракетку слева

igrok1=turtle.Turtle()
igrok1.color('deeppink')
igrok1.shape('square') # придаём ракетке форму
igrok1.shapesize(stretch_len=1,stretch_wid=5)
igrok1.penup() # чтобы ракетка не оставляла следов
igrok1.goto(-450,0)

igrok2=turtle.Turtle()
igrok2.color('lightseagreen')
igrok2.shape('square') # придаём ракетке форму
igrok2.shapesize(stretch_len=1,stretch_wid=5)
igrok2.penup() # чтобы ракетка не оставляла следов
igrok2.goto(450,0)

# счет игроков

bal1=0
b1=turtle.Turtle(visible=False)
b1.color('hotpink')
b1.penup()
b1.setposition(-200,300)
b1.write(bal1,font=("Cooper Black",44))

bal2=0
b2=turtle.Turtle(visible=False)
b2.color('turquoise')
b2.penup()
b2.setposition(200,300)
b2.write(bal1,font=("Cooper Black",44))

#надписи
nadp=turtle.Turtle(visible=False)
nadp.color('salmon')
nadp.penup()
nadp.setposition(-150,350)
nadp.write("It's GAME!",font=("Cooper Black",50))

nadp_vih=turtle.Turtle(visible=False)
nadp_vih.color('powderblue')
nadp_vih.penup()
nadp_vih.setposition(260,-350)
nadp_vih.write("To exit press F",font=("Cooper Black",25))

nadp_ws=turtle.Turtle(visible=False)
nadp_ws.color('lightpink')
nadp_ws.penup()
nadp_ws.setposition(-650,0)
nadp_ws.write("W↑  S↓",font=("Calibri",25,"bold"))

nadp_ud=turtle.Turtle(visible=False)
nadp_ud.color('aquamarine')
nadp_ud.penup()
nadp_ud.setposition(530,0)
nadp_ud.write("Up ↑  Down ↓",font=("Calibri",25,"bold"))

# привяжем клавиши игроку

def vverh1(): # создаём функции для движения вниз и вверх
    y=igrok1.ycor()+25
    if y>250:
        y=250
    igrok1.sety(y)
def vniz1():
    y = igrok1.ycor()-25
    if y < -250:
        y = -250
    igrok1.sety(y)
def vverh2():
    y = igrok2.ycor() + 25
    if y > 250:
        y = 250
    igrok2.sety(y)
def vniz2():
    y = igrok2.ycor() - 25
    if y < -250:
        y = -250
    igrok2.sety(y)
def vihod():
    okno.bye()

#создаём мячик
shar=turtle.Turtle()
shar.shape('circle')
shar.speed(0) # чтобы после выхода за поле мячик мгновенно был в середине
shar.shapesize(stretch_wid=1)
shar.color('yellow')
shar.dx=3
shar.dy=-3
shar.penup()

okno.listen()
okno.onkeypress(vverh1,"w")
okno.onkeypress(vniz1,"s")
okno.onkeypress(vverh2,"Up")
okno.onkeypress(vniz2,"Down")
okno.onkeypress(vihod,"f")

# создаём цикл для мячика
while True:
    okno.update()
    shar.setx(shar.xcor()+shar.dx)
    shar.sety(shar.ycor()+shar.dy)
    if (shar.ycor()>=290) or (shar.ycor()<=-290):
        shar.dy=-shar.dy
    if (shar.xcor()>=490):
        bal2 += 1
        b2.clear()
        b2.write(bal2, font=("Cooper Black",44))
        shar.goto(0,randint(-150,150))
        shar.dx = choice([-4,-3,-2,2,3,4])
        shar.dy = choice([-4,-3,-2,2,3,4])
    if (shar.xcor() <=-490):
        bal1 += 1
        b1.clear()
        b1.write(bal1, font=("Cooper Black",44))
        shar.goto(0, randint(-150, 150))
        shar.dx = choice([-4, -3, -2, 2, 3, 4])
        shar.dy = choice([-4, -3, -2, 2, 3, 4])
    if (shar.ycor()>=igrok1.ycor()-50) and (shar.ycor()<=igrok1.ycor()+50) \
            and (shar.xcor()>=igrok1.xcor()-5) and (shar.xcor()<=igrok1.xcor()+5):
        shar.dx = -shar.dx
    if (shar.ycor() >= igrok2.ycor() - 50) and (shar.ycor() <= igrok2.ycor() + 50) \
            and (shar.xcor() >= igrok2.xcor() - 5) and (shar.xcor() <= igrok2.xcor() + 5):
        shar.dx = -shar.dx

okno.mainloop() # чтобы окно не закрывалось