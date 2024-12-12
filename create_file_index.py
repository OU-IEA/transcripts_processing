from pathlib import Path
import os
from dotenv import load_dotenv
from src.index import create_index
import asyncio

load_dotenv()

uga_image_path = Path(os.getenv("IMAGE_PATH_UGA"))
uga_index_path = uga_image_path / "UGA_Index"

sturec_image_path = Path(os.getenv("IMAGE_PATH_STUREC"))
sturec_index_path = sturec_image_path / "STUREC_Index"


if __name__ == "__main__":
    asyncio.run(create_index(uga_index_path))
    asyncio.run(create_index(sturec_index_path))
