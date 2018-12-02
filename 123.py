from tkinter import *
import random

# создаем окно
root = Tk()
root.title("Виселица")
canvas = Canvas(root, width=800, height=600)
canvas.pack()


# фон клетка
def main():
    y = 0
    while y < 600:
        x = 0
        while x < 800:
            canvas.create_rectangle(x, y, x + 45, y + 55, fill="white", outline="black",width = 1)
            x += 45
        y += 55


title = """       Hellow , gamer. 
  Are you reade to play? """
faq = """\t\t\t\t           ПРАВИЛА
     
     Компьютер загадывает слово и выводит такое количество подчёркиваний, сколько букв в слове. 
     Игрок начинает называть буквы, чтобы отгадать слово. 
     Если буква есть в слове, то компьбтер впишет её на своё место в слово (если таких букв несколько — 
     то вписываются все),а если нет — то выводится элемент виселицы с человечком ."""

canvas.create_text(400, 300, text=faq, fill="black", font=("Helvetica", "12"))
canvas.create_text(400, 150, text=title, fill="blue", font=("Arial", "20"))

words = ["абсцисса", "авантюра", "автограф", "агрессор", "баклажан", "бактерия",
         "банкнота", "работник", "разведка", "шевелюра", "таинство", "таксофон", "талисман",
         "давление", "дворянин", "фанатизм", "фельдшер", "завалина", "языковед"]


def random_word():
    main()
    random_worde = random.choice(words)
    w = random_worde[1:]
    chek_word = []
    for i in w:
        chek_word.append(i)
    let0 = canvas.create_text(480, 200, text=random_worde[0], fill="green", font=("Arial", "30"))
    let1 = canvas.create_text(510, 200, text="_", fill="green", font=("Aria black", "30"))
    let2 = canvas.create_text(540, 200, text="_", fill="green", font=("Arial bLack", "30"))
    let3 = canvas.create_text(570, 200, text="_", fill="green", font=("Arial black", "30"))
    let4 = canvas.create_text(600, 200, text="_", fill="green", font=("Arial black", "30"))
    let5 = canvas.create_text(630, 200, text="_", fill="green", font=("Arial black", "30"))
    let6 = canvas.create_text(660, 200, text="_", fill="green", font=("Arial black", "30"))
    let7 = canvas.create_text(690, 200, text="_", fill="green", font=("Arial black", "30"))

    unknown_latters = [1, 2, 3, 4, 5, 6, 7]
    alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    false = []
    true = []

    # сравнивающая функция
    def classification(letter):
        ind_alf = alfabet.index(letter)
        key = alfabet[ind_alf]

        if letter in chek_word:
            flag = False

            while not flag:

                ind = chek_word.index(letter)
                b2 = unknown_latters[ind]
                chek_word[ind] = '1'

                def coords():
                    if b2 == 1:
                        x1, y1 = 510, 200
                    if b2 == 2:
                        x1, y1 = 540, 200
                    if b2 == 3:
                        x1, y1 = 570, 200
                    if b2 == 4:
                        x1, y1 = 600, 200
                    if b2 == 5:
                        x1, y1 = 630, 200
                    if b2 == 6:
                        x1, y1 = 660, 200
                    if b2 == 7:
                        x1, y1 = 690, 200
                    return x1, y1

                x1, y1 = coords()

                true.append(letter)

                a2 = canvas.create_text(x1, y1, text=w[ind], fill="blue", font=("Arial", "20"))
                button[key]["bg"] = "green"

                if letter not in chek_word:
                    button[key]["state"] = "disabled"
                    flag = True

            if len(true) == 7:
                canvas.create_text(410, 390, text="You win!", fill="blue", font=("Arial", "32"))
                for i in alfabet:
                    button[i]["state"] = "disabled"
        else:
            false.append(letter)
            button[key]["bg"] = "red"
            button[key]["state"] = "disabled"
            if len(false) == 1:
                def stick1():
                    canvas.create_line(50, 50, 50, 550, width=6, fill="brown")
                    root.update()

                stick1()
            elif len(false) == 2:
                def stick2():
                    canvas.create_line(50, 50, 200, 50, width=6, fill="brown")
                    root.update()

                stick2()
            elif len(false) == 3:
                def loop():
                    canvas.create_line(200, 50, 200, 200, width=3, fill="gray")
                    root.update()

                loop()
            elif len(false) == 4:
                def head():
                    canvas.create_oval(170, 200, 230, 250, width=3)
                    canvas.create_line(190, 215, 192, 216, width=6, fill="black")
                    canvas.create_line(210, 215, 208, 216, width=6, fill="black")
                    canvas.create_line(185, 235, 215, 235, width=4, fill="pink")
                    root.update()

                head()
            elif len(false) == 5:
                def body():
                    canvas.create_line(200, 250, 200, 350, width=3, fill="black")
                    root.update()

                body()
            elif len(false) == 6:
                def arms():
                    canvas.create_line(200, 275, 230, 315, width=3)
                    canvas.create_line(200, 275, 170, 315, width=3)

                arms()
            elif len(false) == 7:
                def legs():
                    canvas.create_line(200, 350, 230, 450, width=4)
                    canvas.create_line(200, 350, 170, 450, width=4)

                legs()
                Loose()
            root.update()

    button = {}

    # кнопки

    def alfabet_button(u, x, y):

        button[u] = Button(root, text=u, width=3, height=1, command=lambda: classification(u))
        button[u].place(x=str(x), y=str(y))

    x = 450
    y = 250
    for i in alfabet[0:8]:
        alfabet_button(i, x, y)
        x += 33
    x = 450
    y = 280
    for i in alfabet[8:16]:
        alfabet_button(i, x, y)
        x += 33
    x = 450
    y = 310
    for i in alfabet[16:24]:
        alfabet_button(i, x, y)
        x += 33
    x = 450
    y = 340
    for i in alfabet[24:33]:
        alfabet_button(i, x, y)
        x += 33

    def Loose():
        canvas.create_text(410, 390, text="You died!", fill="red", font=("Arial", "32"))
        for i in alfabet:
            button[i]["state"] = "disabled"


def Exit():
    exit()


button_1 = Button(root, text="Start", width=20, height=3, command=lambda: random_word())
button_1.place(x=150, y=500)
button_1["bg"] = "lightgray"

button_2 = Button(root, text="Exit", width=20, height=3, command=lambda: Exit())
button_2.place(x=500, y=500)
button_2["bg"] = "lightgray"

root.mainloop()
