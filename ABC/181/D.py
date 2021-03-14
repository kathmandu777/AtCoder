import sys
import copy

li = [int(s) for s in list(input())]
if (len(li) == 1):
    li.append(0)
    li.append(0)
elif (len(li) == 2):
    li.append(0)

eight_li = [8, 16, 24, 32,  48, 56, 64, 72, 88, 96,  112, 128, 136, 144, 152, 168,
            176, 184, 192, 216, 224, 232,  248, 256, 264, 272,  288, 296, 312, 328, 336, 344, 352,  368, 376, 384, 392,  416, 424, 432,  448, 456, 464, 472, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640, 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744, 752, 760, 768, 776, 784, 792, 800, 808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904, 912, 920, 928, 936,
            944, 952,  968, 976, 984, 992]

for i in range(len(eight_li)):
    li_sub = [int(s) for s in list(str(eight_li[i]))]

    if (len(li_sub) == 1):
        li_sub.append(0)
        li_sub.append(0)
    elif (len(li_sub) == 2):
        li_sub.append(0)
    # print(li_sub)

    copy_li = copy.copy(li)
    # print(copy_li)
    if (copy_li.count(li_sub[0]) > 0):
        copy_li.remove(li_sub[0])
        if (copy_li.count(li_sub[1]) > 0):
            copy_li.remove(li_sub[1])
            if (copy_li.count(li_sub[2]) > 0):
                copy_li.remove(li_sub[2])
                print("Yes")
                sys.exit()

print("No")
