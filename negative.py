#To compute the negative of an imge and display the image.

from PIL import Image
img  = Image.open("C:/Users/ekta/Desktop/flowers.jpg") 
for y in range(img.height):
    for x in range(img.width):
        value = img.getpixel((x, y))
        new_color = (255-value[0], 255-value[1], 255-value[2])
        img.putpixel((x, y), new_color)
img.save('output2.png')