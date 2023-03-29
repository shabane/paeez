#!/usr/bin/env python3
from PIL import Image
import os.path


def createThumnail(source_path: str, dest_path: str, quality: int=50) -> None:
    if not os.path.exists(source_path):
        FileExistsError('source file does not exist')
    img = Image.open(source_path)
    assert quality >= 1 and quality <= 100, ValueError('quality should not be lower than 1 and higher than 100')
    if not os.path.exists(os.path.dirname(dest_path)):
        FileNotFoundError('destionation directory not found')
    img.save(dest_path, optimize=True, quality=quality)


if __name__ == '__main__' :
    print('reducing image quality...\n')
    createThumnail(
        source_path=input('Enter source file path: '),
        dest_path=input('Enter destination file path: '),
        quality=int(input('Enter quality: '))
    )
