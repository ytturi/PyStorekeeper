# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os.path import isfile, isdir
from json import loads
import logging

from PyStorekeeper.logging import initialize_logger, verbose_log


_CONFS = {}


def get_config(argname, default=False):
    """
    Check for a configuration in the config dictionary
    :type argname:  str
    :param argname: Key for the configuration

    :type default:  value
    :param default: Default value for the configuration if does not exist

    :return:    Value of the configuration key if exists, else _default_
    """
    if argname not in _CONFS:
        verbose_log('{} is not found in confs!', 'debug', confs=_CONFS)
    return _CONFS.get(argname, default)


def initialize(verbose_level=0, store_type='test', conf_path=None):
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
    # Default configs
    _CONFS.update({
        'verbose':verbose_level, # Min verbosity before setting
        'archive_compression': 'tar.gz',
    })
    if conf_path:
        verbose_log('Using config file {}'.format(conf_path), 'info', 1)
        if isfile(conf_path):
            with open(conf_path, 'r') as conf_file:
                _CONFS.update(loads(conf_file.read()))
        else:
            verbose_log('Conf file not found!', 'error')
            return False
    # Fix confs from args
    #   Verbosity
    if verbose_level != 0: # Override confs with command-line args
        _CONFS.update({'verbose':verbose_level})
    #   Store type
    if store_type == 'files':
        _CONFS.update({'filesystem_archive': True})
    verbose_log('Confs:', 'info', 2)
    for conf_key, conf_data in _CONFS.items():
        verbose_log('\t- {}: {}'.format(conf_key, conf_data), 'info', 2)
    verbose_log('Loaded confs')
    return _CONFS
