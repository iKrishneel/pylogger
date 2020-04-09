#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import coloredlogs


FORMAT = '[%(levelname)s] \033[31m%(lineno)s\033[0m:%(module)s/%(funcName)s\n\t%(message)s'


def get_logger(logger_name, level='DEBUG'):
    logger = logging.getLogger(logger_name)
    coloredlogs.install(
        fmt=FORMAT,
        level=level,
        logger=logger)
    return logger
