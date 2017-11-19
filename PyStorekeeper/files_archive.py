from utils import verbose_log
from os.path import isfile, isdir

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
    verbose_log('Archiving path {}'.format(filesystem_path), 'info')
    return True

