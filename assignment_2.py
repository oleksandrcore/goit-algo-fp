import turtle

def draw_pythagoras_tree(level, size, angle):
    if level == 0:
        return

    turtle.forward(size)
    turtle.left(angle)
    draw_pythagoras_tree(level-1, size*0.7, angle)
    turtle.right(angle*2)
    draw_pythagoras_tree(level-1, size*0.7, angle)
    turtle.left(angle)
    turtle.backward(size)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    size = 100
    angle = 45

    turtle.speed(0)
    turtle.penup()
    turtle.goto(-size/2, -size/2)
    turtle.pendown()

    draw_pythagoras_tree(level, size, angle)

    turtle.done()

if __name__ == "__main__":
    main()