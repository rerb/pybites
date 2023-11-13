import pathlib


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    if type(path) not pathlib.PosixPath:
        path = pathlib.Path(directory) 
    dirs = files = 0
    for inode in path.iterdir():
        if inode.is_dir():
            dirs += 1
            for sub_dirs, sub_files in count_dirs_and_files(directory / inode.name):
                dirs += sub_dirs
                files += sub_files
        else:
            files += 1
    return (dirs, files)