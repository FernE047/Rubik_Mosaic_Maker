import os
from PIL import Image

#resize every image to 200x200

for filename in sorted(os.listdir("really_pieces")):
    if filename.endswith(".png"):
        img = Image.open("really_pieces/" + filename)
        img = img.resize((200, 200))
        img.save("real_pieces/" + filename)