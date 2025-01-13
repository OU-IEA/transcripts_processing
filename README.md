
# Desc

To install on Windows:
-  download and install latest version of Tesseract from [here](https://github.com/tesseract-ocr/tesseract/releases)

- clone repository, create virtual environment and activate it
- install Python dependencies listed in `requirements.txt`. If you get an error installing `tesserocr` library, download and install Windows Build from [here](https://github.com/simonflueckiger/tesserocr-windows_build) and then reinstall dependencies again.

## Flow

Parameters are in defined in the `.env` file. Modify accordingly.
- `create_file_index.py` creates a csv file with file index, which contains file name, path and student PID.

- `count_files.py` provides count of files by different type. It can be used to examine the structure of the folders and what they contain.

- `prepare_ocr.py` sets up and creates necessary scaffolding for the Optical Character Recognition (OCR) process.

- `perform_ocr.py` runs ocr process using image files and outputting final results in json format. The script uses `multiprocessing` pool of workers, which means it will use 100% of your CPU. You can specify maximum number of workers if necessary. Refer to  the [documentation](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor). You can interrupt ocr process and resume it later. The script will pick up where it left off. To do that, simply kick off the script. Do not run `prepare_ocr.py` again. 

## Other
- `tesseract.R` is an example of how to use Tesseract inside R. This is pretty much analogous to Python version. Fully functional, comparable in speed and tested.
