from PyStorekeeper.utils import *
from PyStorekeeper import files_archive
import click
import os


@click.command()
@click.option('-v', '--verbose',
    default=0, type=int, help='Verbose level to log')
@click.option('-c', '--config',
    default='', type=str, help='Configuration file to import (JSON)')
def py_archive(verbose, config):
    confs = initialize(verbose_level=verbose, conf_path=config)
    fs_paths = confs.get('paths', [])
    for fs_path in fs_paths:
        files_archive.archive_path(fs_path)
