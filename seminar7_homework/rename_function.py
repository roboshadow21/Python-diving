from pathlib import Path


def rename_files(filename: str, digits: int, extension_src: str, extension_dst: str,
                 lower_border: int, upper_border: int) -> None:
    path = Path.cwd()
    pattern1 = '*.' + extension_src
    pattern2 = '.' + extension_dst
    counter = 0

    for path in path.glob(pattern1):
        name = path.name
        path.rename(name[lower_border:upper_border] + filename + str(counter) * digits + pattern2)
        counter += 1
