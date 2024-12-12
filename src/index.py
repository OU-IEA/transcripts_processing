from pathlib import Path
import aiofiles
import pandas as pd
import numpy as np

from loguru import logger


@logger.catch
async def create_index(index_path: Path) -> None:
    async with aiofiles.open(index_path, mode="r") as index:
        content = await index.readlines()

    data = np.asarray(content).reshape(-1, 4)
    df = pd.DataFrame(
        data=data, columns = ["file_handle", "pid", "export_date", "file_path"]
    )
    df = df.apply(lambda x: x.str.replace("\n", ""))

    parent_path = index_path.parent.parent
    file_name = index_path.name

    save_path = parent_path / (file_name + ".csv")
    df.to_csv(save_path, index=False)
    print(f"Index file saved at {save_path}")
