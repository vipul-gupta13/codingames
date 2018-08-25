import sys
import math
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
xi = yi  = 0
xf = w - 1 
yf = h - 1

while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir.find("U")>-1:
        yf = y0 - 1
    elif bomb_dir.find("D")>-1:
        yi = y0 + 1
    if bomb_dir.find("L")>-1:
        xf = x0 - 1
    elif bomb_dir.find("R")>-1:
        xi =x0 + 1
    x0 = int(xi + int((xf  - xi)/2))
    y0 = int(yi + int((yf  - yi)/2))
    # the location of the next window Batman should jump to.
    print(x0, y0)
