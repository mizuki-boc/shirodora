from PIL import Image, ImageDraw
import glob
#
# #im = Image.new("RGB", (500, 300), (128, 128, 128))
# # im = Image.open("免許証.png")
# # draw = ImageDraw.Draw(im)
# #色
#green = (0, 255, 0)
# #枠のカラー
#clr = green
# #画像の縁取り
# #直線，(始点のx座標, 始点のy座標, 終点のx座標, 終点のy座標)
"""
for img_name in glob.glob("i_*.png"):
    im = Image.open(img_name)
    draw = ImageDraw.Draw(im)
    draw.line(((0, 0), (im.size[0], 0), im.size, (0, im.size[1]), (0, 0)), fill=clr, width=10)
    im.save('test/{}_test.png'.format(img_name), quality=95)

img_name = "i_skl_260x280.png"
im = Image.open(img_name)
draw = ImageDraw.Draw(im)
test = ((0,0), (im.size[0],0), im.size, (0,im.size[1]), (0,0))
draw.line(((0,0), (im.size[0],0), im.size, (0,im.size[1]), (0,0)), fill=80, width=10)
im.save("test.png", quality=95)

img_name = "i_aag_260x280.png"
waku_w2 = 32
photo = Image.open(img_name)
canvas = Image.new("RGBA", (photo.size[0]+waku_w2, photo.size[1]+waku_w2), (128,128,128))
draw = ImageDraw.Draw(canvas)
draw.line((0, 0, canvas.width, 0), fill=(0, 255, 0), width=waku_w2)
draw.line((canvas.width, 0, canvas.width, canvas.height), fill=(0, 255, 0), width=waku_w2)
draw.line((canvas.width, canvas.height, 0, canvas.height), fill=(0, 255, 0), width=waku_w2)
draw.line((0, canvas.height, 0, 0), fill=(0, 255, 0), width=waku_w2)
canvas.paste(photo, (waku_w2//2, waku_w2//2, waku_w2//2+photo.size[0], waku_w2//2+photo.size[1]))
canvas.show()
"""

def main():
    for img_name in glob.glob("i_*.png"):
        waku_w2 = 32
        photo = Image.open(img_name)
        canvas = Image.new("RGBA", (photo.size[0]+waku_w2, photo.size[1]+waku_w2), (128,128,128))
        draw = ImageDraw.Draw(canvas)
        draw.line((0, 0, canvas.width, 0), fill=(0, 255, 0), width=waku_w2)
        draw.line((canvas.width, 0, canvas.width, canvas.height), fill=(0, 255, 0), width=waku_w2)
        draw.line((canvas.width, canvas.height, 0, canvas.height), fill=(0, 255, 0), width=waku_w2)
        draw.line((0, canvas.height, 0, 0), fill=(0, 255, 0), width=waku_w2)
        canvas.paste(photo, (waku_w2//2, waku_w2//2, waku_w2//2+photo.size[0], waku_w2//2+photo.size[1]))
        canvas.save("green_img/grn_{}".format(img_name))

if __name__ == "__main__":
    main()
