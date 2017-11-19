# -*- coding: utf-8 -*-
from os.path import isfile, isdir
from json import loads
import logging


def _log_msg(msg='', log_type='info'):
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


def initialize(verbose_level=0, conf_path=None):
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
    if verbose_level != 0: # Override confs with command-line args
        confs.update({'verbose':verbose_level})
    verbose_log('Confs:', 'info', 1)
    for conf_key, conf_data in confs.items():
        verbose_log('\t- {}: {}'.format(conf_key, conf_data), 'info', 1)
    verbose_log('Loaded confs')
    return confs
