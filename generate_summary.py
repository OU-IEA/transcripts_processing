from pathlib import Path
from dotenv import load_dotenv
import os
from src.helpers import count_files, Style


load_dotenv()
os.system("")

dir_path = [Path(os.getenv("IMAGE_PATH_STUREC")), Path(os.getenv("IMAGE_PATH_UGA"))]


if __name__ == "__main__":
    for folder in dir_path:
        ext_counts = count_files(folder, True)
        print(f"Total file counts inside of {Style.GREEN}{str(folder)}{Style.RESET} are:")
        for extension, count in ext_counts.items():
            print(f"{extension :<10} {count:>6}")
            total = sum(ext_counts.values())
        print(f"{Style.YELLOW}{'Total' :<10} {total:>6}{Style.RESET}", end ="\n\n")