big_list = marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
counter1 = 0
while counter1 < len(big_list):
    small_list_length = len(big_list[counter1])
    counter2 = 0
    max_num = 0
    while counter2 < small_list_length:
        if big_list[counter1][counter2]>max_num:
            max_num = big_list[counter1][counter2]
        counter2 = counter2 + 1
    print max_num
   # print big_list[counter1][counter2-1]
    counter1 = counter1 + 1
    print '-----'
