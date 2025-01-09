from pathlib import Path
from dotenv import load_dotenv
from src.utils import create_directory, move_files
import os
import pickle
from loguru import logger


def main():
    create_directory(image_output_path)
    create_directory("temp")

    # move pdf and db files to skipped_files
    create_directory(image_path / "skipped_files")
    move_files(
        image_path, ["*.pdf", "*.PDF", ".db"], Path(image_path / "skipped_files")
    )

    # save all image files to pickle; they will be loaded in during ocr step
    in_files = set(image_path.glob("*.*"))
    with open("temp/ocr_input_files.pkl", "wb") as f:
        pickle.dump(in_files, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    load_dotenv()
    image_path = Path(os.getenv("IMAGE_PATH_STUREC"))
    image_output_path = Path(image_path, "json_ocr_output")

    main()

    # writing to log file
    logger.add("temp/ocr_processed.log")
