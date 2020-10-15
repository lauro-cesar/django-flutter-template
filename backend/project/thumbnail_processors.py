from PIL import Image, ImageDraw


def circle_processor(im, bang=False, **kwargs):
    try:
        bigsize = (im.size[0] * 3, im.size[1] * 3)
        mask = Image.new("L", bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(im.size, Image.ANTIALIAS)
        im.putalpha(mask)
        return im
    except Exception:
        print("error PIL")
        return im
