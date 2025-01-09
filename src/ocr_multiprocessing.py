import cv2
from tesserocr import PyTessBaseAPI, PSM, OEM
from PIL import Image
import os
from pathlib import Path
import json
from loguru import logger

logger.add("issues.log")


@logger.catch
def ocr(img_path):
    os.environ["OMP_THREAD_LIMIT"] = "1"
    custom_config = {
        "tessedit_char_blacklist": "*|{}[]()<>_+=^%$#@!~`?",
    }
    with PyTessBaseAPI(
        path="C:\\Program Files\\Tesseract-OCR\\tessdata",
        psm=PSM.AUTO,
        oem=OEM.DEFAULT,
        variables=custom_config,
    ) as api:
        outfile = img_path.with_suffix(".json")
        outfile = outfile.parent / "json_output" / outfile.name

        if not outfile.exists():
            # minor preprocessing and file read
            img = cv2.imread(img_path)
            img = cv2.copyMakeBorder(
                img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 255]
            )
            text = Image.fromarray(img)

            # extracting text
            api.SetImage(text)
            translated_text = api.GetUTF8Text()
            transcript = {
                "file_handler": img_path.stem,
                "transcript": translated_text,
            }

            with open(outfile, "w") as outfile:
                with open("temp/ocr_processed.log", "a") as log:
                    log.write(f"{img_path}\n")
                    json.dump(transcript, outfile, indent=4)
