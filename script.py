"""
    Checks and removes all required directories
"""
import logging
import os
import shutil
import sys
import arrow

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def execute():
    """
        Execute loop for all directories
    """
    loop_root()

def remove_path(entry):
    """
        Remove one directory and log
    """
    itemtime = arrow.get(entry.stat().st_mtime)
    shutil.rmtree(entry.path)
    logging.info('The "%s" directory with creation date %s was removed.',
                 entry.path, itemtime)

def is_dir(entry):
    """
        Checks if it's a valid directory
    """
    return not entry.name.startswith('.') and entry.is_dir()

def is_old(entry):
    """
        Checks if directory is older than configured
    """
    criticaltime = arrow.now().shift(seconds=-int(os.getenv('TIME_TO_REMOVE_SECONDS')))
    itemtime = arrow.get(entry.stat().st_mtime)
    return itemtime < criticaltime

def work_with_watch(path):
    """
        Receives an observed directory, checks its contents to see if the item should
        be deleted, and exclude
    """
    with os.scandir(path) as dirs:
        for entry in dirs:
            if is_dir(entry):
                if is_old(entry):
                    remove_path(entry.path)

def loop_root():
    """
        Loop in the root directory to find all directories observed.
    """
    filespath = './watch/'
    with os.scandir(filespath) as dirs:
        for entry in dirs:
            work_with_watch(entry.path)


if __name__ == '__main__':
    execute()
