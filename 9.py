import turtle
import math


def draw_circle(t, x, y, radius, color="black"):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.circle(radius)


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def analyze_circles(x1, y1, r1, x2, y2, r2):
    distance = calculate_distance(x1, y1, x2, y2)

    sum_radii = r1 + r2
    diff_radii = abs(r1 - r2)

    if distance > sum_radii:
        return "Окружности лежат одна вне другой, не касаясь"
    elif distance == sum_radii:
        return "Окружности имеют внешнее касание"
    elif diff_radii < distance < sum_radii:
        return "Окружности пересекаются"
    elif distance == diff_radii:
        return "Окружности имеют внутреннее касание"
    else:  # distance < diff_radii
        return "Одна окружность лежит внутри другой, не касаясь"


def main():
    print("Введите координаты центра и радиус первой окружности:")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    r1 = float(input("r1 = "))

    print("\nВведите координаты центра и радиус второй окружности:")
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    r2 = float(input("r2 = "))

    screen = turtle.Screen()
    screen.title("Анализ двух окружностей")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    draw_circle(t, x1, y1, r1, "blue")

    draw_circle(t, x2, y2, r2, "red")

    result = analyze_circles(x1, y1, r1, x2, y2, r2)
    print(f"\nРезультат анализа: {result}")

    t.penup()
    t.goto(-200, -250)
    t.color("black")
    t.write(result, font=("Arial", 14, "normal"))

    t.goto(-200, -280)
    t.write("Синяя окружность - первая, Красная - вторая", font=("Arial", 12, "normal"))

    print("\nНажмите любую клавишу, чтобы закрыть окно...")
    input()
    screen.bye()


if __name__ == "__main__":
    main()
