"""
Bulk converts images of subsequent file type into .tiff:
                                                        .png
                                                        .jpg
                                                        .jpeg
                                                        .bmp
                                                    
                                                    
You need to specify the "directory" for the correct file path to your image folder.

The exif dictionary in the script contains information about the image file, such as the orientation. The Orientation key in the exif dictionary contains a value that represents the orientation of the image. This value can be one of several different values, each of which represents a different orientation.

The if exif['Orientation'] == 3: line is checking if the value of the Orientation key in the exif dictionary is equal to 3. If it is, it means that the image is in "upside-down" orientation and should be rotated 180 degrees to display correctly. The script then uses the im.rotate(180, expand=True) method to rotate the image 180 degrees, so that it will be displayed correctly when it is saved as a TIFF file.

The other if statements are checking for other values of the Orientation key, for example:

    if exif['Orientation'] == 6: it means that the image is rotated 90 degrees clockwise and should be rotated to 270 degrees to display correctly.
    if exif['Orientation'] == 8: it means that the image is rotated 90 degrees counter-clockwise and should be rotated to 90 degrees to display correctly.

This way, the script makes sure that the image is correctly oriented before saving it as a TIFF file.

"""


import os
from PIL import Image, ExifTags

directory = "/Users/tobias/Pictures/OCR_TEST"
output_path = "/tiff"

def bulk_convert_to_tiff():

    image_files = [f for f in os.listdir(directory) if f.endswith((".jpg", ".jpeg", ".png", ".bmp"))]

    output_directory = os.path.join(directory, "output")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for image_file in image_files:
        
        with Image.open(os.path.join(directory, image_file)) as im:
            
            exif = {ExifTags.TAGS[k]: v for k, v in im._getexif().items() if k in ExifTags.TAGS}
            
            if 'Orientation' in exif:
                if exif['Orientation'] == 3:
                    im = im.rotate(180, expand=True)
                elif exif['Orientation'] == 6:
                    im = im.rotate(270, expand=True)
                elif exif['Orientation'] == 8:
                    im = im.rotate(90, expand=True)

            tiff_file = os.path.splitext(image_file)[0] + ".tiff"

            im.save(os.path.join(output_directory, tiff_file))


    
if __name__ == '__main__':
    bulk_convert_to_tiff()