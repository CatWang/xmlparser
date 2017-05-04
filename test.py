#coding:utf-8
from PIL import Image
from PIL.ImageDraw import ImageDraw
from xml.dom.minidom import parse
import xml.dom.minidom
import xml.etree.ElementTree as ET

root = ET.parse("words.xml")
images = root.findall("image")

index = 1

with open('ryoungt.csv', 'w') as csvfile:
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
            x = float(taggedRectangle.get("x"))
            y = float(taggedRectangle.get("y"))
            width = float(taggedRectangle.get("width"))
            height = float(taggedRectangle.get("height"))

            box = (x, y, x + width, y + height)
            region = im.crop(box)
            filename = "ryoungt/" + str(index) + ".jpg"
            region.save(filename)
            csvfile.write('%s %s\n' % (filename, tag))
            index = index + 1









