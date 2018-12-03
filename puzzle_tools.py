#coding:utf-8
import os

BLACK_P = 255
WHITE_P = 0

class FindGap(object):
    def get_curve(self, im):
        wid = im.size[0]
        hei = im.size[1]

        # im = im.convert('1')
        # x_start = 0
        # y_start = 0
        arr = []
        for x in range(7, 19):
            for y in range(hei):
                rgb = im.getpixel((x, y))[:3]
                if rgb[0] == BLACK_P:
                    arr.append((x, y))
                    break

        return arr

    def find_match(self, im, arr):
        wid = im.size[0]
        hei = im.size[1]

        # x = 257
        # arr_b = []
        # for x in range(x, x+12):
        #     for y in range(hei):
        #         rgb = im.getpixel((x, y))[:3]
        #         if rgb[0] == 0:
        #             arr_b.append((x, y))
        #             break
        # for ind in range(len(arr)):
        #     print arr[ind], arr_b[ind]
        # return

        # 最大的像素中断次数
        MAX_MISS_C = 2
        # 最小连续的像素
        MIN_CONTINUE = 10
        # y 方向允许的像素波动
        WAVE_Y = 1

        arr_ind = 0
        x_start = None
        arr_len = len(arr)

        miss_c = 0
        for x in range(wid):
            # for y in range(hei):
            y = arr[arr_ind][1]
            match_y = False
            for y in range(y-WAVE_Y, y + WAVE_Y + 1):
                rgb = im.getpixel((x, y))[:3]
                if rgb[0] == WHITE_P:
                    match_y = True
                    break
            if match_y:
                if x_start is None:
                    x_start = x
                arr_ind += 1
            else:
                if miss_c >= MAX_MISS_C:
                    x_start = None
                    arr_ind = 0
                    miss_c = 0
                else:
                    miss_c += 1
                    arr_ind += 1

            # print x_start, arr_ind
            if arr_ind > MIN_CONTINUE:
                break

        return x_start

def RGB2BlackWhite(im):
    print "image info,", im.format, im.mode, im.size
    (w, h) = im.size
    R = 0
    G = 0
    B = 0

    for x in xrange(w):
        for y in xrange(h):
            pos = (x, y)
            rgb = im.getpixel(pos)
            (r, g, b) = rgb[:3]
            R = R + r
            G = G + g
            B = B + b

    rate1 = R * 1000 / (R + G + B)
    rate2 = G * 1000 / (R + G + B)
    rate3 = B * 1000 / (R + G + B)

    print "rate:", rate1, rate2, rate3

    for x in xrange(w):
        for y in xrange(h):
            pos = (x, y)
            rgb = im.getpixel(pos)
            (r, g, b) = rgb[:3]
            n = r * rate1 / 1000 + g * rate2 / 1000 + b * rate3 / 1000
            # print "n:",n
            if n >= 60:
                im.putpixel(pos, (255, 255, 255))
            else:
                im.putpixel(pos, (0, 0, 0))
    return im

# im = img_a.convert('RGB')

# for num in range(1, 6):
#     path = os.path.join('pic', 'b', str(num) + '.jpeg')
#     img = Image.open(path)
#     img = img_handler.RGB2BlackWhite(img)
#     img.show()

# for num in range(1, 6):
#     path = os.path.join('pic', 'a', str(num) + '.png')
#     img = Image.open(path)
#     img = img_handler.RGB2BlackWhite(img)
#     find_a(img)



# pic_num = 5
# img_a = Image.open(r'pic\a\%d.png'%pic_num)
# img = img_handler.RGB2BlackWhite(img_a)
#
# arr = find_a(img)
#
# img = Image.open(r'pic\b\%d.jpeg'%pic_num)
# img = img_handler.RGB2BlackWhite(img)
#
#
# x_start = find_b(img, arr)
#
# print x_start













