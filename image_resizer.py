# Use your Terminal, if you are on
# Windows type: python image_resizer.py
from PIL import Image

img = Image.open("./img/img.png")
img.thumbnail((250, 250))
img.save("./img_resize/img_resize.png")
print(img.size)
