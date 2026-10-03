import tkinter as tk

janela = tk.Tk()
janela.title("Breakout")

canvas = tk.Canvas(janela, width=400, height=400, bg="black")
canvas.pack()

pontos = 0
vx, vy = 3, -3

raquete = canvas.create_rectangle(160, 370, 240, 380, fill="#8603db")
bola = canvas.create_oval(195, 340, 205, 350, fill="white")

texto = canvas.create_text(50, 15, text="Pontos: 0", fill="white")

tijolos = []

for linha in range(2):
    for coluna in range(10):
        x = coluna * 40
        y = 30 + linha * 20

        tijolos.append(canvas.create_rectangle(x + 2, y, x + 38, y + 15, fill="cyan"))


def esquerda(event):
    x1, y1, x2, y2 = canvas.coords(raquete)

    if x1 > 0:
        canvas.move(raquete, -20, 0)


def direita(event):
    x1, y1, x2, y2 = canvas.coords(raquete)

    if x2 < 400:
        canvas.move(raquete, 20, 0)


janela.bind("<Left>", esquerda)
janela.bind("<Right>", direita)


def jogo():
    global vx, vy, pontos

    canvas.move(bola, vx, vy)

    x1, y1, x2, y2 = canvas.coords(bola)

    # Paredes
    if x1 <= 0 or x2 >= 400:
        vx *= -1

    if y1 <= 0:
        vy *= -1

    # Raquete
    r = canvas.coords(raquete)

    if x2 >= r[0] and x1 <= r[2] and y2 >= r[1]:
        vy *= -1

    # Tijolos
    for tijolo in tijolos[:]:

        t = canvas.coords(tijolo)

        if x2 >= t[0] and x1 <= t[2] and y2 >= t[1] and y1 <= t[3]:

            canvas.delete(tijolo)
            tijolos.remove(tijolo)

            vy *= -1
            pontos += 1

            canvas.itemconfig(texto, text=f"Pontos: {pontos}")

            break

    # Final
    if pontos == 20:

        canvas.create_text(
            200, 200, text="VOCÊ VENCEU!", fill="white", font=("Arial", 25)
        )

    elif y2 >= 400:

        canvas.create_text(200, 200, text="GAME OVER", fill="white", font=("Arial", 25))

    else:
        janela.after(20, jogo)


jogo()
janela.mainloop()
