#!/usr/bin/env python

import logging

from .logger import ColoredLogger


logging.setLoggerClass(ColoredLogger)


def get_logger(name: str):
    return logging.getLogger(name)

