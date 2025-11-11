from turtle import Screen

def tecla_presionada(key):
    print(f"Presionaste: {key}")

screen = Screen()
screen.listen()

# Detecta cualquier tecla
for t in ["Up", "Down", "Left", "Right", "space", "w", "s", "i", "k"]:
    screen.onkey(lambda t=t: tecla_presionada(t), t)

screen.mainloop()
