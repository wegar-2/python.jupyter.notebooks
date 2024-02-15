from pathlib import Path
import zipfile
from loguru import logger


if __name__ == "__main__":

    dir_to_zip: Path = Path(__file__).parent.parent / "data"
    archive_name: str = "data.zip"
    dir_target: Path = Path(__file__).parent / archive_name
    unzip_target: Path = Path(__file__).parent / "data_unzipped"

    if dir_target.exists():
        raise FileExistsError(f"Directory {dir_target} exists!")

    with zipfile.ZipFile(dir_target, "w") as archive:
        for file in dir_to_zip.iterdir():
            if file.is_file():
                logger.info(f"adding to archive: {file}")
                archive.write(filename=file, arcname=file.name)

    logger.info(f"Unzipping into: {unzip_target}")
    with zipfile.ZipFile(dir_target, "r") as archive:
        for file in archive.namelist():
            logger.info(f"unzipping {file} into {unzip_target}")
            archive.extract(member=file, path=unzip_target)
