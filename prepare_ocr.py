from pathlib import Path
from dotenv import load_dotenv
from src.utils import create_directory
import os
import pickle
from loguru import logger


def main():
    create_directory(image_output_path)
    create_directory("temp")
    in_files = set(image_path.glob('*.*'))
    with open('temp/ocr_input_files.pkl','wb') as f:
        pickle.dump(in_files,f, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    
    load_dotenv()
    image_path = Path(os.getenv("IMAGE_PATH_STUREC"))
    image_output_path = Path(image_path,'json_output')

    main()
    logger.add("temp/ocr_processed.log")



    