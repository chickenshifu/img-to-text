"""
docstring
"""

import pytesseract
from pytesseract import Output
from PIL import Image
import cv2
import os
from helperFunctions import chronograph, print_color



tess_config = r"--psm 4 --oem 3" #needs to be adjusted
tess_lang = 'deu'

tiff_path ='/Users/tobias/Pictures/OCR_TEST/output'
tiff_files = [f for f in os.listdir(tiff_path) if f.endswith((".tiff"))]

for tiff in tiff_files:
    img_path = f'{tiff_path}/{tiff}'
    print_color('green', f'Parsing: {tiff}\n__________________________')
    print(pytesseract.image_to_string(Image.open(img_path), lang=tess_lang))
    

resized_list = []

for tiff in tiff_files:
    print_color('blue', f'__________________________\nOpening {tiff}\n')
    
    img_path = f'{tiff_path}/{tiff}'
    img = cv2.imread(img_path, 1)
    
    height, width, _ = img.shape
    
    scale_percent = 100 # percent of original size

    print_color('blue', f'Resizing to {scale_percent}% of its original value...\n')

    width_for_resizing = int(img.shape[1] * scale_percent / 100)
    height_for_resizing = int(img.shape[0] * scale_percent / 100)
    dim = (width_for_resizing, height_for_resizing)

    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11) #no good results

    # # Apply the Laplacian operator to the grayscale image
    # laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # # Convert the result back to an 8-bit unsigned integer
    # laplacian = cv2.convertScaleAbs(laplacian)

    # # Add the sharpened image to the original image
    # sharpened = cv2.addWeighted(gray, 1.5, laplacian, -1.5, 0)


    print_color('blue', f'Creating boxes for {tiff}...\n')

    data = pytesseract.image_to_data(gray, config=tess_config, output_type=Output.DICT)
    
    confidences_list = data["conf"]
    overall_confidence = round(sum(confidences_list) / len(confidences_list), 2)

    print_color("green", f'Overall confidence: {overall_confidence} %')

    amount_boxes = len(data['text'])
    for i in range(amount_boxes):
        if float(data['conf'][i]) > 80:
                (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                img = cv2.rectangle(gray, (x, y), (x+width, y+height), (0, 255, 0), 2)
                img = cv2.putText(gray, data['text'][i], (x, y+height+17), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)


    cv2.imshow(f'Image: {tiff}', gray)
    cv2.waitKey(0)
