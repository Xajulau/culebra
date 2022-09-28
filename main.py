import turtle
import time
import random

retrasar = 0.1

#configuracion Ventana
vt = turtle.Screen()
vt.title("Culebra")
vt.bgcolor("black")
vt.setup(width= 600, height=600)
vt.tracer()

# configuracion serpiente
bolo = turtle.Turtle()
bolo.speed(0)
bolo.shape("square")
bolo.color("yellow")
bolo.penup()
bolo.goto(0,0)
bolo.direction = "stop"

#Raton que se come
raton = turtle.Turtle()
raton.speed(0)
raton.shape("triangle")
raton.color("brown")
raton.penup()
raton.goto(0,100)
raton.direction = "stop"

#cuerpo serpiente
segmento = []

# cursores
def paraarriba():
    bolo.direction = "arriba"
def paraabajo():
    bolo.direction = "abajo"
def paraizquierda():
    bolo.direction = "izquierda"
def paraderecha():
    bolo.direction = "derecha"



def mov():
    if bolo.direction == "arriba":
        y=bolo.ycor()
        bolo.sety(y + 20)
    if bolo.direction == "abajo":
        y=bolo.ycor()
        bolo.sety(y - 20)
    if bolo.direction == "izquierda":
        x=bolo.xcor()
        bolo.setx(x - 20)
    if bolo.direction == "derecha":
        x=bolo.xcor()
        bolo.setx(x + 20)

#teclado
vt.listen()
vt.onkeypress(paraarriba,"Up")
vt.onkeypress(paraabajo,"Down")
vt.onkeypress(paraizquierda,"Left")
vt.onkeypress(paraderecha,"Right")

while True:
    vt.update()

    if bolo.distance(raton) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        raton.goto(x,y)

        nuevosegmento = turtle.Turtle()
        nuevosegmento.speed(0)
        nuevosegmento.shape("square")
        nuevosegmento.color("grey")
        nuevosegmento.penup()
        segmento.append(nuevosegmento)

    #mover cuerpo serpiente
    totalseg = len(segmento)
    for i in range(totalseg -1, 0, -1):
        x = segmento[i - 1].xcor()
        y = segmento[i - 1].ycor()
        segmento[i].goto(x,y)

    if totalseg > 0:
        x = bolo.xcor()
        y = bolo.ycor()
        segmento[0].goto(x,y)

    mov()
    time.sleep(retrasar)
