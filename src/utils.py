from pathlib import Path
import collections
from typing import Union
from tqdm import tqdm
from loguru import logger
import itertools

logger.add("issues.log")


@logger.catch
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


class Style:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"


@logger.catch
def create_directory(directory_path: Union[str, Path]) -> None:
    directory_path = Path(directory_path)
    if not directory_path.exists():
        directory_path.mkdir(parents=True)
        print(f"Output directory created at {Style.GREEN}{directory_path}{Style.RESET}")


@logger.catch
def read_log(filename) -> set:
    with open(filename, "r") as file:
        lines = file.readlines()
        return set(Path(line.strip()) for line in lines)


def get_image_files(image_path: Path) -> set:
    file_patterns = [
        "*.tif",
        "*.jpg",
        "*.png",
        "*.jpeg",
        "*.tiff",
        "*.JPG",
        "*.JPEG",
        "*.PNG",
        "*.TIF",
        "*.TIFF",
    ]

    files = set(
        itertools.chain.from_iterable(
            image_path.glob(pattern) for pattern in file_patterns
        )
    )
    return files
