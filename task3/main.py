import tkinter as tk
import random

root = tk.Tk()
root.title("Bonus Collector Game")

canvas = tk.Canvas(root, width=500, height=400, bg="lightblue")
canvas.pack()

character = canvas.create_rectangle(230, 350, 270, 370, fill="red")

score = 0

score_label = tk.Label(root, text=f"Score: {score}", font=("Helvetica", 16))
score_label.pack()


def move_left(event):
    canvas.move(character, -20, 0)


def move_right(event):
    canvas.move(character, 20, 0)


root.bind("<Left>", move_left)
root.bind("<Right>", move_right)


def create_bonus():
    x = random.randint(20, 480)
    y = 0
    if random.choice([True, False]):
        bonus = canvas.create_oval(x, y, x+20, y+20, fill="gold")
        return bonus, "bonus"
    else:
        anti_bonus = canvas.create_oval(x, y, x+20, y+20, fill="black")
        return anti_bonus, "anti-bonus"


def move_objects():
    global score
    for obj, obj_type in objects:
        canvas.move(obj, 0, 5)
        obj_pos = canvas.coords(obj)
        if obj_pos[1] >= 400:
            canvas.delete(obj)
            objects.remove((obj, obj_type))
        elif obj_pos[1] >= 350:
            char_pos = canvas.coords(character)
            if char_pos[0] < obj_pos[2] and char_pos[2] > obj_pos[0]:
                if obj_type == "bonus":
                    score += 1
                    score_label.config(text=f"Score: {score}")
                elif obj_type == "anti-bonus":
                    end_game()
                canvas.delete(obj)
                objects.remove((obj, obj_type))
    root.after(50, move_objects)


def end_game():
    canvas.create_text(250, 200, text="Game Over", font=("Helvetica", 32), fill="red")
    root.unbind("<Left>")
    root.unbind("<Right>")


objects = []


def create_objects():
    if random.random() < 0.1:
        obj, obj_type = create_bonus()
        objects.append((obj, obj_type))
    root.after(500, create_objects)


create_objects()
move_objects()

root.mainloop()
