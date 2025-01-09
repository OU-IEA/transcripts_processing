from pathlib import Path
from dotenv import load_dotenv
from src.utils import create_directory, get_image_files
import os
import pickle
from loguru import logger


def main():
    create_directory(image_output_path)
    create_directory("temp")

    # save all image files to pickle; they will be loaded in during ocr step
    in_files = get_image_files(image_path)
    print(f"Number of files to be processed: {len(in_files)}")
    with open("temp/ocr_input_files.pkl", "wb") as f:
        pickle.dump(in_files, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    load_dotenv()
    image_path = Path(os.getenv("IMAGE_PATH_STUREC"))
    image_output_path = Path(image_path, "json_ocr_output")

    main()

    # writing to log file
    logger.add("temp/ocr_processed.log")
