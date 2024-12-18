import os
from pathlib import Path
import concurrent.futures
from dotenv import load_dotenv
from src.ocr_multiprocessing import ocr
import time

load_dotenv()

image_path = Path(os.environ.get('TEST'))
files = list(image_path.glob('*'))

os.environ['OMP_THREAD_LIMIT'] = '1'

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        for i in zip(files,executor.map(ocr,files)):
            print('processed')
 
if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)