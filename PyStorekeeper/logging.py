# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os.path import isfile, isdir
from json import loads
import logging


def _log_msg(msg='', log_type='info'):
     """
     Private method to log messages using logger
     :param msg:      Message to log
     :type msg:       str
     :param log_type: Log type (from logging) to use
     :type log_type:  str
     :return:         TRUE if logged with any of the available log_types
     :rtype:          bool
     """
     logger = logging.getLogger('pystorekeeper')
     if log_type.lower() == 'info':
         logger.info(msg)
         return True
     elif log_type.lower() == 'warning':
         logger.warning(msg)
     elif log_type.lower() == 'debug':
         logger.debug(msg)
         return True
     elif log_type.lower() == 'error':
         logger.error(msg)
         return True
     elif log_type.lower() == 'critical':
         logger.critical(msg)
         return True
     return False
   

def verbose_log(msg=False, log_type='info', level=0, confs=None):
    """
    Method to log using logger type and verbose level from confs
    :param msg:      Message to log
    :type msg:       str
    :param log_type: Logging type to use
    :type log_type:  str
    :param level:    Verbose level required to log the message
    :type level:     int
    :return:         TRUE if message is logged, else FALSE
    :rtype:          bool
    """
    logger = logging.getLogger()
    if confs is not None:
        verb_level = confs.get('verbose', -1)
    else:
        from PyStorekeeper.config_manager import get_config
        verb_level = get_config('verbose', -1)
    if not verb_level and level != 0:
        return False
    elif not verb_level and level == 0:
        return _log_msg(msg, log_type)
    elif verb_level and verb_level >= level:
        return _log_msg(msg=msg, log_type=log_type)
    return False

def initialize_logger():
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s | %(message)s',
        datefmt='%Y/%m/%d-%H:%M:%S',
        level=logging.NOTSET
    )
    logging.addLevelName(logging.INFO, '  INFO  ')
    logging.addLevelName(logging.ERROR, '  ERROR ')
    logging.addLevelName(logging.DEBUG, '  DEBUG ')
    logging.addLevelName(logging.CRITICAL, 'CRITICAL')
    logging.addLevelName(logging.WARNING, ' WARNING')