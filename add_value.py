#To import an image and add a value to all pixels and display the image

from PIL import Image
img  = Image.open("C:/Users/ekta/Desktop/flowers.jpg") 
red_tint = int(input("Red tint: "))
green_tint = int(input("Green tint: "))
blue_tint = int(input("Blue tint: "))
red, green, blue = img.split()
for y in range(img.height):
    for x in range(img.width):
        value = img.getpixel((x, y))
        new_color = (value[0] + int(red_tint), value[1] + int(green_tint), value[2] + int(blue_tint))
        img.putpixel((x, y), new_color)
img.save('output1.png')