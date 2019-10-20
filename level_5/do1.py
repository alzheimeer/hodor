#!/usr/bin/python3
""" Deobfuscate IMAGE"""
from PIL import Image


def obf(pn, l1=10):
    '''obf'''
    img = Image.open(pn)
    img = img.convert('RGB')
    p1 = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if (p1[x, y][0] < l1) and (p1[x, y][1] < l1) and (p1[x, y][2] < l1):
                p1[x, y] = (0x80, 0x80, 0x80, 255)

    img.show()
    img.save('o.png')
