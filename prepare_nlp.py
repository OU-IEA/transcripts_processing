from pathlib import Path
from dotenv import load_dotenv
from src.utils import create_directory
import pickle
import os
from loguru import logger


def main():
    create_directory(nlp_output_path)
    create_directory("temp")

    # save all image files to pickle; they will be loaded in during ocr step
    in_files = set(Path(image_path / "json_ocr_output").glob("*.json"))
    print(f"Number of files to be processed: {len(in_files)}")
    with open("temp/nlp_input_files.pkl", "wb") as f:
        pickle.dump(in_files, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    load_dotenv()
    image_path = Path(os.getenv("IMAGE_PATH_UGA"))
    nlp_output_path = Path(image_path / "json_nlp_output")

    main()

    # writing to log file
    logger.add("temp/nlp_processed.log")
