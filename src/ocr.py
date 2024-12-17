import os
from tesserocr import PyTessBaseAPI, PSM, OEM
import cv2
from PIL import Image
import csv
import json
import time


class OCR:
    """
    A class that performs OCR on images in a directory and saves the output in a directory
    Documents are output to directory preserve progress if the program is interrupted
    """
    
    
    def __init__(self, image_path: str, csv_path: str, output_path: str):
        """
        Initializes the ocr class
        """
        self.image_path = image_path
        self.csv_path = csv_path
        self.output_path = output_path
        self.original_thread_count = os.environ.get('OMP_THREAD_LIMIT', None)
        
        
    def process_image(self, image):
        
        """
        Processes the image before running OCR on it.
        This includes removing noise, removing row and column lines and enhancing the text.
        """
        
         
        image = cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255,255,255])
        #remove noise
        image = cv2.GaussianBlur(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), (3,3), 0)
        _, image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)
        #get rows
        horiz_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (100,1))
        morph = cv2.morphologyEx(image, cv2.MORPH_CLOSE, horiz_kernel)
        contours, hierarchy = cv2.findContours(morph, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        rows = [None] * len(contours)
        for i, c in enumerate(contours):
            rows[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
        rows = sorted(rows, key=lambda x: x[1])
        #get columns
        vert_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,50))
        vert_morph = cv2.morphologyEx(image, cv2.MORPH_CLOSE, vert_kernel)
        contours, hierarchy = cv2.findContours(vert_morph, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        image = cv2.drawContours(image, contours, 0, (0,255,0), 3)
        cols = [None] * len(contours)
        for i, c in enumerate(contours):
            cols[i] = cv2.boundingRect(cv2.approxPolyDP(c, 3, True))
        cols = sorted(cols, key=lambda x: x[0])
        #removing row and column lines
        _,image = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV)
        image = cv2.bitwise_and(morph,image)
        image = cv2.bitwise_and(vert_morph,image)
        kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(10,2))
        mask = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel2)
        return image
    

    def run_ocr(self):
        """
        Runs Tesseract(OCR) on all images in the image_path directory and saves the output in the output_path directory
        
        """
        #this ensures that tesseract uses only one thread because it is more efficient that way
        os.environ['OMP_THREAD_LIMIT'] = '1'
        with open(self.csv_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            num_files = len(os.listdir(self.image_path))
            try:
                with PyTessBaseAPI(path='/usr/share/tesseract-ocr/4.00/tessdata', psm=PSM.AUTO, oem = OEM.DEFAULT) as api:
                
                    for i, row in enumerate(csv_reader):
                        total_start = time.time()
                        image_start = 0
                        image_stop = 0
                        ocr_start = 0
                        ocr_stop = 0
                        if row[3].endswith(('.tif', '.jpg', '.png', '.jpeg', '.tiff', '.JPG', '.JPEG', '.PNG', '.TIF', '.TIFF')):
                            filename = row[3][row[3].rfind('\\')+1:]
                            img_location = os.path.join(self.image_path, filename)
                            image_start = time.time()
                            img = cv2.imread(img_location)
                            #img = self.process_image(img)
                            pil_image = Image.fromarray(img)
                            image_stop = time.time()
                            ocr_start = time.time()
                            api.SetImage(pil_image)
                            translated_text = api.GetUTF8Text()
                            ocr_stop = time.time()
                            transcript = {
                                "PID": row[1],
                                "Transcript": translated_text,
                            }
                            json_object = json.dumps(transcript, indent = 4)    
                            with open(self.output_path + '/'+ row[0] +'.json','w') as outfile:
                                outfile.write(json_object)
                        total_stop = time.time()
                        print(f'{i}/{num_files} completed')
                        print(f'(image-processing:{image_stop-image_start:.2f}s    ocr-processing: {ocr_stop-ocr_start:.2f}s    total: {total_stop-total_start:.2f}s)')
            except Exception as e:
                print(e)
            #os.environ['OMP_THREAD_LIMIT'] = self.original_thread_count
   
            
            
        
        
        
        