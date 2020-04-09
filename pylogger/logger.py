#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
import coloredlogs


def get_logger(logger_name, level='DEBUG'):
    logger = logging.getLogger(logger_name)
    coloredlogs.install(
        fmt='%(filename)s:%(lineno)d %(asctime)s - [%(levelname)s] %(message)s',
        level=level, logger=logger)
    return logger
