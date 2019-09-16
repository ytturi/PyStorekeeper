from PyStorekeeper.config_manager import initialize
from PyStorekeeper.logging import initialize_logger, verbose_log
from PyStorekeeper import files_archive
import click
import os


@click.command()
@click.option('-v', '--verbose',
    default=0, type=int, help='Verbose level to log [0: None - 5: full]')
@click.option('-c', '--config',
    default='', type=str, help='Configuration file to import (JSON)')
@click.option(
    '-t', '--store-type', type=click.Choice(['files', 'test']),
    default='test', show_default=True,
    help='Type of archives to store')
def py_archive(verbose=0, config=False, store_type=False):
    initialize_logger()
    confs = initialize(
        verbose_level=verbose,
        store_type=store_type,
        conf_path=config
    )
    exit()
    if not confs:  # Could not load confs
        exit(-1)
    merge_paths = []
    if confs.get('filesystem_archive', False):
        fs_paths = confs.get('paths', [])
        for fs_path in fs_paths:
            merge_paths.append(files_archive.archive_path(fs_path))
    if merge_paths:
        verbose_log(
            'Merging {} file{} into a backup archive'.format(
                len(merge_paths), 's ' if len(merge_paths) > 1 else ' '
        ))
    else:
        verbose_log('There are no backuped files to merge!', 'error')
