import turtle
import time
import math


def draw_rect_prism(p1x, p1y, p1z, p2x, p2y, p2z, p3x, p3y, p3z, p4x, p4y, p4z, p5x, p5y, p5z, p6x, p6y, p6z, p7x, p7y,
                    p7z, p8x, p8y, p8z):
    #turtle.begin_fill()
    turtle.color('blue')
    # front face
    draw_line(p1x, p1y, p1z, p2x, p2y, p2z)
    draw_line(p2x, p2y, p2z, p3x, p3y, p3z)
    draw_line(p3x, p3y, p3z, p4x, p4y, p4z)
    draw_line(p4x, p4y, p4z, p1x, p1y, p1z)
    #turtle.end_fill()
    # left face
    #turtle.begin_fill()
    turtle.color('blue')
    draw_line(p4x, p4y, p4z, p8x, p8y, p8z)
    draw_line(p8x, p8y, p8z, p5x, p5y, p5z)
    draw_line(p5x, p5y, p5z, p1x, p1y, p1z)
    #turtle.end_fill()
    # back face
    #turtle.begin_fill()
    turtle.color('blue')
    draw_line(p5x, p5y, p5z, p6x, p6y, p6z)
    draw_line(p6x, p6y, p6z, p7x, p7y, p7z)
    draw_line(p7x, p7y, p7z, p8x, p8y, p8z)
    #turtle.end_fill()
    # right face
    #turtle.begin_fill()
    turtle.color('blue')
    draw_line(p6x, p6y, p6z, p2x, p2y, p2z)
    draw_line(p2x, p2y, p2z, p3x, p3y, p3z)
    draw_line(p3x, p3y, p3z, p7x, p7y, p7z)
    #turtle.end_fill()
    # top face
    #turtle.begin_fill()
    turtle.color('blue')
    draw_line(p5x, p5y, p5z, p1x, p1y, p1z)
    draw_line(p6x, p6y, p6z, p2x, p2y, p2z)
    #turtle.end_fill()
    # bottom face
    #turtle.begin_fill()
    turtle.color('blue')
    draw_line(p7x, p7y, p7z, p3x, p3y, p3z)
    draw_line(p8x, p8y, p8z, p4x, p4y, p4z)
    #turtle.end_fill()


def calculate_trig():
    global sine_x
    global cosine_x
    global sine_y
    global cosine_y

    sine_x = math.sin(x_rotation)
    cosine_x = math.cos(x_rotation)

    sine_y = math.sin(y_rotation)
    cosine_y = math.cos(y_rotation)


def draw_line(a, b, c, d, e, f):
    set_point_1(a - camera_x_pos, b - camera_y_pos, c - camera_z_pos)
    set_point_2(d - camera_x_pos, e - camera_y_pos, f - camera_z_pos)

    set_point_1(z1 * sine_y + x1 * cosine_y, y1, z1 * cosine_y - x1 * sine_y)
    set_point_2(z2 * sine_y + x2 * cosine_y, y2, z2 * cosine_y - x2 * sine_y)

    set_point_1(x1, y1 * cosine_x - z1 * sine_x, y1 * sine_x + z1 * cosine_x)
    set_point_2(x2, y2 * cosine_x - z2 * sine_x, y2 * sine_x + z2 * cosine_x)

    set_secondary_points(FOV * x1 / z1, FOV * y1 / z1, FOV * x2 / z2, FOV * y2 / z2)

    turtle.goto(x1, y1)
    turtle.pd()
    turtle.goto(x2, y2)
    turtle.pu()


def set_secondary_points(a, b, c, d):
    global x1
    global y1
    global x2
    global y2

    x1 = a
    y1 = b

    x2 = c
    y2 = d


def set_point_1(a, b, c):
    global x1
    global y1
    global z1

    x1 = a
    y1 = b
    z1 = c


def set_point_2(a, b, c):
    global x2
    global y2
    global z2

    x2 = a
    y2 = b
    z2 = c


sine_x = float(0)
cosine_x = float(0)
sine_y = float(0)
cosine_y = float(0)

turtle.ht()
turtle.pu()

FOV = 90 # original: 205

camera_x_pos = float(0)
camera_y_pos = float(0)
camera_z_pos = float(-500)

x_rotation = float(0) #does not work
y_rotation = float(-0.75) #1.25 is max for z = -500

x1 = float(-20)
y1 = float(20)
z1 = float(-20)
x2 = float(20)
y2 = float(20)
z2 = float(-20)

calculate_trig()
turtle.speed(0)

while 1 == 1:
    draw_rect_prism(-100, 100, -100, 100, 100, -100, 100, -100, -100, -100, -100, -100, -100, 100, 100, 100, 100, 100, 100, -100, 100, -100, -100,100)