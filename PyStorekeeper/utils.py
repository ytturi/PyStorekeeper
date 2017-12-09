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
     logger = logging.getLogger()    
     if log_type.lower() == 'info':
         logger.info(msg)
         return True
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
   

def verbose_log(msg=False, log_type='info', level=0):
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
    if 'confs' not in globals().keys():
        logger.error('Trying to log without initialize!')
    verb_level = confs.get('verbose', -1)
    if not verb_level and level != 0:
        return False
    elif not verb_level and level == 0:
        return _log_msg(msg, log_type)
    elif verb_level and verb_level >= level:
        return _log_msg(msg=msg, log_type=log_type)
    return False


def get_config(argname, default=False):
    if argname not in confs:
        verbose_log('{} is not found in confs!', 'debug')
    return confs.get(argname, default)


def initialize(verbose_level=0, conf_path=None):
    """
    Method to initialize the Storekeeper
    - Init logger with a formatter and level
    - Init confs with default values
    - Import confs from configuration file if provided
    :param verbose_level: Verbose level provided by command_line args
    :type verbose_level:  int
    :param conf_path:     Configuration file path to read and import
    :type conf_path:      str
    :return:              Configurations using default confs and imported
    :rype:                dict
    """
    logging.basicConfig(
        format='%(asctime)s%(levelname)s| %(message)s',
        datefmt='[%Y/%m/%d-%H:%M:%S]',
        level=logging.INFO
    )
    global confs
    # Default configs
    confs = {
        'verbose':verbose_level,
        'archive_compression': 'tar.gz',
    }
    if conf_path:
        verbose_log('Using config file {}'.format(conf_path), 'info', 1)
        if isfile(conf_path):
            with open(conf_path, 'r') as conf_file:
                confs.update(loads(conf_file.read()))
        else:
            verbose_log('Conf file not found!', 'error')
            return False
    if verbose_level != 0: # Override confs with command-line args
        confs.update({'verbose':verbose_level})
    verbose_log('Confs:', 'info', 2)
    for conf_key, conf_data in confs.items():
        verbose_log('\t- {}: {}'.format(conf_key, conf_data), 'info', 2)
    verbose_log('Loaded confs')
    return confs
