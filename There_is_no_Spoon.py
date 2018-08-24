# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

p = [[1 for wq in range(width)] for hq in range(height)]

# for h in range(height):
#     for w in range(width):
#         # print("p[" + str(h) + "]" + "[" + str(w) + "] = " + str(p[h][w]) )
#         print(p[h][w], end=' ')
#     print(" ")

for hw in range(height):
    line = input()  # width characters, each either 0 or .
    # line = '0.0.0'
    for wh in range(width):
        if str(line[wh]) == '0':
            p[hw][wh] = 0

# for h in range(height):
#     for w in range(width):
#         # print("p[" + str(h) + "]" + "[" + str(w) + "] = " + str(p[h][w]) )
#         print(p[h][w], end=' ')
#     print(" ")

for h in range(height):
    for w in range(width):
        out = ' '
        if p[h][w] == 0:
            out = out + str(w) + " " + str(h) + " "
            fw = 0
            fh = 0
            for w1 in range(w+1, width):
                fw = 1
                if str(p[h][w1]) == '0':
                    out = out + str(w1) + " " + str(h) + " "
                    break
                if w1 == width-1:
                    out = out + "-1 -1 "
            if fw == 0:
                out = out + "-1 -1 "
            for h1 in range(h+1, height):
                fh = 1
                if str(p[h1][w]) == '0':
                    out = out + str(w) + " " + str(h1) + " "
                    break
                if h1 == height-1:
                    out = out + "-1 -1 "
            if fh == 0:
                out = out + "-1 -1 "
            # print("length = " + str(len(out)))
            # print("output = " + out)
            print(out)
