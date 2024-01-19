from PIL import Image

print('We are going to combine and image of a cactus and a beach.')
print('First we have to load the image of our beach. We can do this using image.open from the PIL library.')
image_beach=Image.open('beach.jpg')
print('Next we have to do the same for the image of our cactus.')
image_cactus=Image.open('cactus.jpg')
print('After that we want to make a new variable for the combined image, and create the new image. We can do this using image.new from the PIL library.')
combined_image=Image.new('RGB', image_beach.size)

print('Next we have to store the RGB values for each of our images. That can be done by using image.load form the PIL library. ')
pixels_beach=image_beach.load()
pixels_cactus=image_cactus.load()
pixels_combined=combined_image.load()

width, height=image_beach.size


print('''Now that we have all of the values we need, a nested for loop can change the value of each pixel in our new image 
            by checking certain constraints we set. In this case we will want to set the constraints to be certain greater 
            or less than certain RGB values''')
for x in range (0,width):
    for y in range (0,height):
        (r,g,b)= pixels_cactus[x,y]
        if r<= 150 and g>=215 and b<= 60:
            pixels_cactus[x,y]=pixels_beach[x,y]
        elif r<= 145 and g>=210 and b<=145:
            pixels_cactus[x,y]=pixels_beach[x,y]
        elif r<= 155 and g>=210 and b<=155:
            pixels_cactus[x,y]=pixels_beach[x,y]
        elif r<=230 and g>=254 and b<=230:
            pixels_cactus[x,y]=pixels_beach[x,y]
        elif r<=164 and g>= 164 and b<=84:
            pixels_cactus[x,y]=pixels_beach[x,y]
        elif r<=66 and g>=120 and b<=45:
            pixels_cactus[x,y]=pixels_beach[x,y]
        elif r<=130 and g>=200 and b<=130:
            pixels_cactus[x,y]=pixels_beach[x,y]
        pixels_combined[x,y]=pixels_cactus[x,y]

print('After our for loops run we can save our new image by using image.save and we can show our new image by using image.show.')
combined_image.save('Beach_Cactus.jpg')
combined_image.show()