import concurrent.futures
import pickle

from tqdm import tqdm

from src.ocr_multiprocessing import ocr
from src.utils import read_log


def main_ocr(in_files):
    with tqdm(total=len(in_files)) as progress:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for i in zip(in_files, executor.map(ocr, in_files)):
                progress.update()


if __name__ == "__main__":
    with open("temp/ocr_input_files.pkl", "rb") as f:
        in_files = pickle.load(f)
    processed = read_log("temp/ocr_processed.log")
    to_process = in_files - processed
    print(f"Processing: {len(to_process)} files")
    main_ocr(to_process)
