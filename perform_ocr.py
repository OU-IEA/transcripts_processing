from dotenv import load_dotenv
import  os
from src.ocr import OCR
from src.helpers import create_directory


load_dotenv()
image_path = os.environ.get('IMAGE_PATH_TEST')
csv_path = os.environ.get('FILE_INDEX_PATH')
ocr_output_path = os.environ.get('FILE_JSON_OUPUT_PATH')


if __name__ == '__main__':
    create_directory(ocr_output_path)
    ocr = OCR(image_path, csv_path, ocr_output_path)
    ocr.run_ocr()