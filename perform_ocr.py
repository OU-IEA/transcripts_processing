import concurrent.futures
from src.utils import read_log
from src.ocr_multiprocessing import ocr
from tqdm import tqdm
import pickle 


def main_ocr(in_files):
    with tqdm(total=len(in_files)) as progress:
        with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
            for i in zip(in_files,executor.map(ocr,in_files)):
                progress.update()


if __name__ == '__main__':
    with open('temp/ocr_input_files.pkl','rb') as f:
        in_files = pickle.load(f)
    processed = read_log('temp/ocr_processed.log')
    to_process = in_files - processed
    main_ocr(to_process)