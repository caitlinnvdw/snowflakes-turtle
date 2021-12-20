import turtle
import random

def draw_snowflake(t, x, y, length, angle, depth, length_scale, angle_scale):

    depth -= 1 
    if depth != 0:
        
        draw_spike(t, x, y, length, angle, 4, length_scale, angle_scale)
        draw_snowflake(t, x, y, length, angle + 45, depth, length_scale, angle_scale)

def draw_spike(t, x, y, length, angle, depth, length_scale, angle_scale):
    t.penup()
    t.setpos(x,y) 
    t.pendown()
    t.setheading(angle)
    t.forward(length)

    last_x, last_y = t.pos()
    depth -= 1
    if depth != 0:
        draw_spike(t, last_x, last_y, length * (length_scale * 0.66), angle + angle_scale, depth, length_scale, angle_scale)
        draw_spike(t, last_x, last_y, length * (length_scale * 0.66), angle - angle_scale, depth, length_scale, angle_scale) 
        draw_spike(t, last_x, last_y, length * length_scale, angle, depth, length_scale, angle_scale)

def main():
    bgcolor_options = ['black', 'dark blue', 'light blue']
    try:
        userchoice_bgcolor = int(input('Choose a color: 0: "Black" , 1: "Dark Blue", 2: "Light Blue"'))
    except ValueError:
        print('Error: value must be a number between 0-2')
        quit()
    if userchoice_bgcolor > len(bgcolor_options):
        print("Value is out of range")
        quit()

    shelly = turtle.Turtle()
    shelly.color('white')
    shelly.shape('turtle')
    window = turtle.Screen()
    window.bgcolor(bgcolor_options[userchoice_bgcolor])
    window.setup(1000, 1000)
    window.tracer(0)

    w = window.window_width()
    h = window.window_height()

    for i in range(50):
        x = random.randrange(-w / 2, w / 2)
        y = random.randrange(-h / 2 , h / 2)
        angle = random.randrange(1, 25)
        length = random.randrange(1, 30)
        depth = random.randrange(9,15)
        angle_scale = random.randrange(-90, 90)
        length_scale = random.randrange(0, 10) * .10
        draw_snowflake(shelly, x, y, length, angle, depth, length_scale, angle_scale)
    window.update()
    window.exitonclick()

if __name__ == '__main__':
    main()