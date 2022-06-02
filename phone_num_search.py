import re
import logging
from pathlib import Path
from shutil import unpack_archive


def main():
    results = []
    pattern = r"\d{3}-\d{3}-\d{4}"

    unzipper()

    zip_dir = Path.cwd() / "zip_files/"
    txt_files = zip_dir.rglob("*.txt")

    for file in txt_files:
        results.append(search(file, pattern))
    else:
        pass
    for res in results:
        if res is not None:
            print(res.group())


def unzipper():
    zip_dir = Path.cwd() / "zip_files/"
    zip_files = zip_dir.rglob("*.zip")

    while True:
        try:
            path = next(zip_files)
        except StopIteration:
            break  # no more files
        except PermissionError:
            logging.exception("permission error")
        else:
            extract_dir = path.with_name(path.stem)
            unpack_archive(str(path), str(extract_dir), "zip")


def search(file, pattern):
    f = open(file, 'r')
    text = f.read()
    match = re.search(pattern, text)

    if match:
        return match
    else:
        pass


if __name__ == '__main__':
    main()
