import turtle

def draw_rectangle(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)

def rectangles_relationship(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2):
    no_overlap = (x2_1 < x1_2 or x2_2 < x1_1 or y2_1 > y1_2 or y2_2 > y1_1)

    if no_overlap:
        return "Прямоугольники лежат вне друг друга, не касаясь"
    else:
        rect1_in_rect2 = (x1_2 <= x1_1 and x2_1 <= x2_2 and y1_2 >= y1_1 and y2_1 >= y2_2)
        rect2_in_rect1 = (x1_1 <= x1_2 and x2_2 <= x2_1 and y1_1 >= y1_2 and y2_2 >= y2_1)

        if rect1_in_rect2 and rect2_in_rect1:
            return "Прямоугольники совпадают"
        elif rect1_in_rect2:
            return "Один прямоугольник лежит внутри другого, не касаясь"
        elif rect2_in_rect1:
            return "Один прямоугольник лежит внутри другого, не касаясь"
        else:
            overlap_x_start = max(x1_1, x1_2)
            overlap_x_end = min(x2_1, x2_2)
            overlap_y_start = min(y1_1, y1_2)
            overlap_y_end = max(y2_1, y2_2)

            overlap_width = overlap_x_end - overlap_x_start
            overlap_height = overlap_y_start - overlap_y_end

            if overlap_width == 0 or overlap_height == 0:
                return "Прямоугольники имеют касание"
            else:
                return "Прямоугольники имеют пересечение"

screen = turtle.Screen()
screen.title("Относительное расположение прямоугольников")
t = turtle.Turtle()
t.speed(0)

print("Введите координаты первого прямоугольника (верхний левый и правый нижний угол):")
x1_1 = float(input("x1 (левый): "))
y1_1 = float(input("y1 (верхний): "))
x2_1 = float(input("x2 (правый): "))
y2_1 = float(input("y2 (нижний): "))

print("\nВведите координаты второго прямоугольника (верхний левый и правый нижний угол):")
x1_2 = float(input("x1 (левый): "))
y1_2 = float(input("y1 (верхний): "))
x2_2 = float(input("x2 (правый): "))
y2_2 = float(input("y2 (нижний): "))

draw_rectangle(t, x1_1, y1_1, x2_1, y2_1)
t.color("blue")
draw_rectangle(t, x1_2, y1_2, x2_2, y2_2)

result = rectangles_relationship(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2)
print(f"\nРезультат: {result}")

t.penup()
t.goto(-300, -250)
t.write(result, font=("Arial", 14, "normal"))

turtle.done()
