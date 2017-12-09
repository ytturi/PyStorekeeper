from utils import verbose_log, get_config
from os import makedirs
from os.path import isfile, isdir, join
from os.path import basename, normpath
from shutil import rmtree
from datetime import datetime
import tarfile

def archive_path(filesystem_path):
    """
    Archive a FileSystem path using the compression method from confs
    :param filesystem_path: FileSystem Path to archive
    :type filesystem_path:  str
    :return:                Return TRUE if archiving was succesful else FALSE
    :rtype:                 bool
    """
    if not filesystem_path:
        verbose_log('Trying to archive empty filesystem path!', 'error')
        return False
    if not isdir(filesystem_path):
        verbose_log('Path {} does not exist', 'error')
        return False
    filesystem_path = normpath(filesystem_path)
    verbose_log('Archiving path {}'.format(filesystem_path))
    # Debian-based default path
    archive_path = get_config('archiving_path', '/opt/py_archive/backups')
    archive_file = get_config('paths', [filesystem_path]).index(filesystem_path)
    archive_file_name = '{}_archived_path_{}'.format(
        datetime.now().strftime('%Y%m%d'), archive_file
    )
    archive_file_path = join(
        archive_path,
        'tmp_{}.tar.gz'.format(archive_file_name)
    )
    archive_file = join(archive_file_path, archive_file_name)
    compression_method = get_config('archive_compression', 'tar.gz')
    if compression_method != 'tar.gz':
        verbose_log('Compression method not supported', 'error')
        return False
    # First step to get a tmp dir
    if isdir(archive_file_path):
        verbose_log('The temp path for the file exists!', 'warning')
    try:
        makedirs(archive_file_path)
        # Second step is to add all path tree to an archive
        with tarfile.open(archive_file_name, 'w:gz') as archive:
            archive.add(filesystem_path, arcname=basename(filesystem_path))
    except Exception as err:
        verbose_log('Could not archive "{}"!'.format(filesystem_path), 'error')
        verbose_log(err.msg, 'error')
        archive_file_name = False
    finally:
        rmtree(archive_file_path)
    return archive_file_name

