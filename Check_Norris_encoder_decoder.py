
def encoder(my_msg):
    bin_result = ''
    for i in my_msg:
        val_bin = bin(ord(i))[2:]
        if len(val_bin) < 7:
            val_bin = '0' + val_bin
        bin_result = bin_result + str(val_bin)

    # print(bin_result)
    lc = ''
    final = ''
    c = ''
    for j in bin_result:
        if lc == j:
            c = c + '0'
        else:
            final = final + ' ' + c
            if j == '1':
                c = '0 0'
            else:
                c = '00 0'
            lc = j
    final = final + ' ' + c
    return final[2:]


def decoder(my_msg):
    counter1 = 0
    b_msg = ''
    for i in my_msg.split():
        counter1 += 1
        if counter1 == 1:
            if i == '0':
                c = '1'
            else:
                c = '0'
        else:
            fc = ''
            counter2 = 0
            for j in i:
                counter2 += 1
            for k in range(counter2):
                fc = fc + c
            counter1 = 0
            b_msg = b_msg + fc

    counter = 0
    c = ''
    final_msg = ''
    for i in b_msg:
        counter += 1
        c = c + i
        if counter == 7:
            # print(chr(int(c, 2)))
            final_msg = final_msg + chr(int(c, 2))
            counter = 0
            c = ''

    return final_msg


msg = "Vipul@1234"
y = encoder(msg)
print(y)
print(decoder(y))