from pathlib import Path
import shutil

def recursive_dir_rm(dir: Path) -> None:
    if dir.is_file():
        dir.unlink()
        return
    elif dir.is_dir():
        contents = list(dir.iterdir())
        if contents:
            for item in contents:
                recursive_dir_rm(item)
        dir.rmdir()
        return

    return

def recursive_dir_copy(source: Path, dest: Path):
    if source.is_file():
        dest = dest.with_suffix(source.suffix)
        shutil.copy2(source, dest)
        return
    elif source.is_dir():
        contents = source.iterdir()
        if contents:
            for item in contents:
                new_dest = dest / item.stem
                if item.is_dir():
                    new_dest.mkdir(parents=True)
                recursive_dir_copy(item, new_dest)
    return


def copy_dir(source, dest) -> None:
    """calls recursive_dir_rm and recursive_dir_copy"""
    # first check that dest directory is empty
    old_dest = Path(dest)
    if old_dest.is_dir():  # explicit '.exists()' not needed, .is_dir() will return false if the dir doesn't exist
        recursive_dir_rm(old_dest)
    new_dest = Path(dest)

    # copy source to destination
    source = Path(source)
    recursive_dir_copy(source, new_dest)
    return