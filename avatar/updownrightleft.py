

n = int(input())

x, y = 1, 1

direction = input().split()

for where in direction:
    x_dir = 0
    y_dir = 0
    if where is 'R':
        x_dir = 1
    elif where is 'L':
        x_dir = -1
    elif where is 'U':
        y_dir = 1
    elif where is 'D':
        y_dir = -1

    if x + x_dir >= 0:
        x = x+x_dir
    if y + y_dir >= 0:
        y = y+y_dir

print(x_dir, y_dir, sep=", ")
