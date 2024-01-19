from PIL import Image #Loads PIL library 

image_original=Image.open('beach.jpg') #opens an image


width, height = image_original.size #dimensions of an images

print(width, height) #prints dimensions

pixels_original = image_original.load() #stores information about pixels in an image 

r, g, b = pixels_original[100, 200]
print(r,g,b,)
r, g, b = pixels_original[100, 300]
print(r,g,b,)
r, g, b = pixels_original[200, 200]
print(r,g,b,)
r, g, b = pixels_original[500, 400]
print(r,g,b,)
r, g, b = pixels_original[100, 100]
print(r,g,b,)


pixels_original[100, 200] = (0, 500, 0)
pixels_original[100, 300] = (150, 0, 150)
pixels_original[200, 200] = (0, 0, 0)
pixels_original[500, 400] = (500, 0, 0)
pixels_original[100, 100] = (120, 400, 300)


image_original.show()
