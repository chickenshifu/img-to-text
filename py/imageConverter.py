




from PIL import Image

# Open the image file
with Image.open("image.jpg") as im:
    # Save the image in TIFF format
    im.save("image.tiff", "TIFF")
    
    
if __name__ == '__main__':
    pass