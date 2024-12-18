import cv2
from tesserocr import PyTessBaseAPI, PSM, OEM
from PIL import Image
import os

def ocr(img_path):
    os.environ['OMP_THREAD_LIMIT'] = '1'
    with PyTessBaseAPI(path='/usr/share/tesseract-ocr/4.00/tessdata', psm=PSM.AUTO, oem = OEM.DEFAULT) as api:
        img = cv2.imread(img_path)
        text = Image.fromarray(img)
        api.SetImage(text)
        translated_text = api.GetUTF8Text()
        return translated_text
