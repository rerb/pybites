import pathlib


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    path = pathlib.Path(directory) if type(directory) is not pathlib.PosixPath else directory
    dirs = files = 0
    for inode in path.iterdir():
        if inode.is_dir():
            dirs += 1
            sub_dirs, sub_files = count_dirs_and_files(directory / inode.name)
            dirs += sub_dirs
            files += sub_files
        else:
            files += 1
    return (dirs, files)
