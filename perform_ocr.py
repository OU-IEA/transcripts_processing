import os
from pathlib import Path
import concurrent.futures
from dotenv import load_dotenv
from src.ocr_multiprocessing import ocr
from src.helpers import create_directory
import time
from tqdm import tqdm


load_dotenv()

uga_image_path = Path(os.getenv("IMAGE_PATH_STUREC"))
uga_image_output_path = Path(uga_image_path,'json_output')

files = list(uga_image_path.glob('*'))
os.environ['OMP_THREAD_LIMIT'] = '1'

def main():
    with tqdm(total=len(files)) as progress:
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            for i in zip(files,executor.map(ocr,files)):
                progress.update()


if __name__ == '__main__':
    create_directory(uga_image_output_path)
    start = time.time()
    main()
    end = time.time()
    print(end-start)