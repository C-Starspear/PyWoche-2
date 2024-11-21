import turtle

fenster = turtle.Screen()
fenster.bgcolor("black")
fenster.title("Mandala mit 32 Quadraten")

mandala = turtle.Turtle()
mandala.speed(3)
mandala.shape("turtle")
mandala.color("white")

farben = [
    "red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta",
    "gold", "navy", "teal", "lime", "pink", "brown", "skyblue", "violet",
    "maroon", "indigo"
]

def zeichne_quadrat():
    for _ in range(4):
        mandala.forward(100)
        mandala.left(90)

for i in range(32):
    mandala.color(farben[i % len(farben)])
    zeichne_quadrat()
    mandala.left(360 / 32)

fenster.mainloop()
