import turtle


def draw_tree(branch_length, level, angle):
    if level == 0:
        return

    turtle.forward(branch_length)
    turtle.left(angle)
    draw_tree(branch_length * 0.7, level - 1, angle)
    turtle.right(2 * angle)
    draw_tree(branch_length * 0.7, level - 1, angle)
    turtle.left(angle)
    turtle.backward(branch_length)


def main():
    recursion_level = int(input("Enter the recursion level: "))
    angle = 30
    branch_length = 100

    turtle.speed('fastest')
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()
    turtle.color("brown")

    draw_tree(branch_length, recursion_level, angle)

    turtle.done()


if __name__ == "__main__":
    main()
