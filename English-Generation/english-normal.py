#coding:utf-8
import Image, ImageDraw, ImageFont
import random
import os

index = 0
fonts = 0

fontDir = "/home/sensetime/fontsSeldom"
font_dir = os.walk(fontDir)

for root, dirs, files in font_dir:
    for f in files:
        fonts = fonts + 1

print fonts

#NOTICE!
#The code in this file write text at the same position on different pictures.
#You can find the vary position solutions in other files


# All letters and combinations that are used to generate
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', '/', '-', '_', '=', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A',
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', '.', '&', '?', '!', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', ':', ';',
           ',', '\'', '\\', '|', '[', ']', '{', '}', 'com', 'edu', 'cn', 'qq', 'QQ', 'www', 'http', 'wechat', 'cn',
           'me', '`', '"',
           'hk', 'jp', 'us']

seed = len(letters)

print seed

with open('30w.csv', 'w') as csvfile:
    csvfile.write('%s %s\n' % ('filename', 'string'))

    hh = 0
    while (hh < 300):
        hh = hh + 1

        rootDir = '/home/sensetime/deepir_test/test_images/class0_normal'
        list_dir = os.walk(rootDir)

        for root, d, fs in list_dir:
            for file in fs:
                image_path = os.path.join(root, file)
                print(image_path)
                im = Image.open(image_path)
                width, height = im.size
                print im.size
                print width
                print height
                print im.mode
                draw = ImageDraw.Draw(im)

                length = random.randint(2, 20)

                ll = length;

                string = ''
                font = random.randint(1, fonts)
                font_select = 1
                print font

                fontDir = "/home/sensetime/fontsSeldom"
                font_dir = os.walk(fontDir)

                path = ""

                for roo, dirs, files in font_dir:
                    print 1
                    for f in files:
                        if(font_select == font):
                            print font
                            path = os.path.join(roo, f)
                            print path
                            break
                        font_select = font_select + 1

                ttfont = ImageFont.truetype(path, 30)

                print path

                while (length > 0):
                    choice = random.randint(0, seed - 1)
                    print letters[choice]
                    string = string + letters[choice]
                    length = length - len(letters[choice])

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

                # watermark = Image.new("RGBA", im.size)
                # waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")

                draw.text((12, 12), string, fill=(r, g, b), font=ttfont)
                t_width, t_height = draw.textsize(unicode(string, 'UTF-8'), font = ttfont)
                print r
                print g
                print b

                print string

                #box = (0, 0, 20 + t_width, 30 + t_height)

                rX = 16 + t_width
                rY = 27 + t_height
		
                box = (8, 12, rX, rY)

                alpha = random.randint(20, 160)

                # watermask = watermark.convert("L").point(lambda x: min(x, alpha))
                #
                # watermark.putalpha(watermask)
                #
                # im.paste(watermark, None, watermark)

                region = im.crop(box)

                index = index + 1

                filename = '30w/' + str(index) + '.jpg'

                fname = str(index) + '.jpg'

                region.save(filename)

                csvfile.write('%s %s\n' % (fname, string))

