#coding:utf-8
from PIL import Image
from PIL.ImageDraw import ImageDraw
from xml.dom.minidom import parse
import xml.dom.minidom
import xml.etree.ElementTree as ET

root = ET.parse("test.xml")
images = root.findall("image")

index = 1

with open('test.csv', 'w') as csvfile:
    csvfile.write('%s %s\n' % ('filename', 'string'))
    for image in images:
        path = image.find("imageName").text
        im = Image.open(path)

        print("111")

        upper = image.find("taggedRectangles")
        taggedRectangles = upper.findall("taggedRectangle")
        for taggedRectangle in taggedRectangles:
            print("222")
            tag = taggedRectangle.find("tag").text
            if(ord(c) >= 128 or ord(c) == 32 for c in  tag):
                continue
            x = int(taggedRectangle.get("x"))
            y = int(taggedRectangle.get("y"))
            width = int(taggedRectangle.get("width"))
            height = int(taggedRectangle.get("height"))

            box = (x, y, x + width, y + height)
            region = im.crop(box)
            filename = "test/" + str(index) + ".jpg"
            region.save(filename)
            csvfile.write('%s %s\n' % (filename, tag))
            index = index + 1









