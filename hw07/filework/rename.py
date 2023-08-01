from pathlib import Path

__all__ = ['rename']


def slice_name(name: str, slices: tuple | list) -> str:
    return name[slices[0]:slices[1]] if slices else None


def rename(new_name: str, ext: str, new_ext: str = None, num_len: int = 0, slices: tuple | list = None,
           path: str = None) -> int:
    renamed_count = 0
    extension = new_ext if new_ext else ext
    workdir = Path(path) if path else Path.cwd()

    for file in workdir.iterdir():
        if file.is_file() and file.suffix == f'.{ext}':
            renamed_count += 1
            name = '_'.join(
                filter(None, (slice_name(file.stem, slices), new_name, f'{renamed_count:0{num_len}d}.{extension}')))
            file.rename(Path(file.parent, name))

    return renamed_count
