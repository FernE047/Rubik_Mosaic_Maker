#This code show what 3X3 pieces of the image are used to create the mosaic
#and then save the pieces in a folder called "pieces" to be able to repro-
#duce the mosaic later in real life.
#it also shows what pieces and rotations are used to create the mosaic.

from PIL import Image
import os

def print_help(filename, rotation, new_image, x, y):
    l = int(filename.split("_")[1].split(".")[0])
    #paste the piece in the new image
    piece = Image.open("real_pieces/" + filename)
    x = x//3 * 200
    y = y//3 * 200
    if rotation == 0:
        new_image.paste(piece, (x, y))
    elif rotation == 1:
        new_image.paste(piece.rotate(90), (x, y))
    elif rotation == 2:
        new_image.paste(piece.rotate(180), (x, y))
    elif rotation == 3:
        new_image.paste(piece.rotate(270), (x, y))
    print((l,rotation),end="")

def compare_images(img1, img2):
    width, height = img1.size
    pixels1 = img1.load()
    pixels2 = img2.load()
    for x in range(width):
        for y in range(height):
            if pixels1[y, x] != pixels2[y, x]:
                return False
    return True

def is_new_piece(piece, mosaic, x, y):
    for filename in os.listdir("pieces"):
        if filename.endswith(".png"):
            other_piece = Image.open("pieces/" + filename)
            if compare_images(piece, other_piece):
                print_help(filename, 0, mosaic, x, y)
                return False
            for i in range(3):
                other_piece = other_piece.rotate(90)
                if compare_images(piece, other_piece):
                    print_help(filename, i+1, mosaic, x, y)
                    return False
    return True

img = Image.open("psyduck.png")
width, height = img.size

mosaic = Image.new("RGB", (width//3 * 200, height//3 * 200))

for y in range(0, height, 3):
    for x in range(0, width, 3):
        piece = img.crop((x, y, x+3, y+3))
        if is_new_piece(piece, mosaic, x, y):
            l = len(os.listdir("pieces"))
            print((l,0),end="")
            print_help("piece_%d.png" % l, 0, mosaic, x, y)
            piece.save("pieces/piece_%d.png" % l)
    print()

mosaic.save("mosaic.png")