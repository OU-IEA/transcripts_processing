from pathlib import Path
import collections
from typing import Union
from tqdm import tqdm

def count_files(directory_path: Union[str, Path], include_subdirectories=False) -> dict:
    if include_subdirectories:
        directory_files = Path(directory_path).rglob("*")
    else:
        directory_files = Path(directory_path).glob("*")
    all_suffixes = [
        "".join(file_path.suffixes)
        for file_path in tqdm(directory_files)
        if file_path.is_file() and file_path.suffix
    ]
    return collections.Counter(all_suffixes)


class Style():
  RED = "\033[31m"
  GREEN = "\033[32m"
  BLUE = "\033[34m"
  YELLOW = "\033[33m"
  RESET = "\033[0m"