def spiral(count=6, r=1200):
    import math
    rotate_x = 0
    rotate_y = 0
    rotate_z = 0
    for i in range(1, count + 1):
        rotate_x += (r / 100. * math.pi)
        rotate_y += (r / 100. * math.pi)
        rotate_y += (r / 100. * math.pi)
        rotate_z = 33
        print(
            f'''<div class="step slide section past" data-x="{math.cos(i)*r}"    data-y="{math.sin(i)*r}"    data-z="{math.log(i)*r}"    data-rotate-x= "{rotate_x}" data-rotate-y="{rotate_y}" data-rotate-z="{rotate_z}">\nSlide {i}\n </div>'''
        )


def circle_layout(count=20, height=1000):
    from math import pi, sin, cos
    radius = (height * count) / (2 * pi) + 800
    x, y, z = 0, 0, 0
    idx, angle = 1, 0
    while angle <= 2 * pi:
        x, y = cos(angle) * radius, sin(angle) * radius
        print(f'''<div class="step slide section past" data-x="{x}"   data-y="{y}"  data-z="{z}" data-rotate-z="{180*angle/pi}">Slide {idx}</div>''')
        angle += 2 * pi / count
        idx += 1
    # data-rotate-x= "{rotate_x}" data-rotate-y="{rotate_y}" data-rotate-z="{rotate_z}"


if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) < 2:
        circle_layout()

    if len(args) == 2:
        circle_layout(int(args[1]))

    if len(args) == 3:
        circle_layout(*[int(i) for i in args[1:3]])
