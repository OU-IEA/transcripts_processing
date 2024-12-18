import cv2
from tesserocr import PyTessBaseAPI, PSM, OEM
from PIL import Image
import os
from pathlib import Path
import json

def ocr(img_path):
    os.environ['OMP_THREAD_LIMIT'] = '1'
    custom_config = {
        'tessedit_char_blacklist': '*|{}[]()<>_+=^%$#@!~`?',
    }
    with PyTessBaseAPI(path='/usr/local/share/tessdata', psm=PSM.AUTO, oem = OEM.DEFAULT,variables=custom_config ) as api:
        img = cv2.imread(img_path)
        img = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255,255,255])
        outfile = img_path.with_suffix('.json')
        text = Image.fromarray(img)
        api.SetImage(text)
        translated_text = api.GetUTF8Text()
        transcript = {"Transcript": translated_text,}
        json_object = json.dumps(transcript, indent = 4)    
        with open(outfile,'w') as outfile:
           outfile.write(json_object)
