#Script to resize, change format & rotate images
import os
from PIL import Image

#Resizes image and rotates it
def geometry(pic):
    im = pic.resize((128, 128))
    im = pic.rotate(270)
    return im

def main():
    for i in os.listdir("."):
        if i.endswith('.jpg'):
            pic = Image.open(i)
            fname, filext = os.path.splitext(i)
            pic = geometry(pic)
            pic.save('converted/' + i, "PNG")

main()

