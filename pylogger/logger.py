#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import datetime
import logging
import coloredlogs
import termcolor


ATTRS = {
    'DEBUG': ['| \uf188 |', 'grey', 'green'],
    'INFO': ['| \uf129 |', 'white', 'green'],
    'WARNING': ['| \uf06a |', 'yellow', 'green'],
    'ERROR': ['| \uf057 |', 'red', 'green'],
    'FATAL': ['| \uf1e2 |', 'red', 'green'],
}

HASH = '\uf292'
MESSAGE = '\uf086'

class Formatter(logging.Formatter):

    def __init__(self, fmt):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        levelname = record.levelname
        if levelname in ATTRS:
            def colored(text):
                return termcolor.colored(
                    text,
                    color=ATTRS[levelname][1],
                    attrs={'bold': True},
                )

            record.levelname = colored(' {:<8}|'.format(record.levelname))
            record.message2 = termcolor.colored(
                record.msg, color='green',
                attrs={})

            asctime = datetime.datetime.fromtimestamp(record.created)
            record.asctime = termcolor.colored(asctime, color='green')

            record.module = termcolor.colored(
                record.module, color='grey', on_color='on_green')
            record.funcName = termcolor.colored(
                record.funcName, color='cyan')
            record.lineno = termcolor.colored(
                record.lineno, color='cyan')

            # record.icon = ATTRS[levelname][0]
            record.hash = termcolor.colored(HASH, attrs={'dark'})
            record.icon = colored(ATTRS[levelname][0])
            record.message_icon = colored(MESSAGE)
            
        return logging.Formatter.format(self, record)

class ColoredLogger(logging.Logger):

    FORMAT = (
        # '[%(levelname)s] %(module)s:%(funcName)s:%(lineno)s - %(message)s'
        ' %(icon)s%(levelname)s' +\
        '%(hash)s %(lineno)s %(module)s.%(funcName)s\n' +\
        '%(message_icon)s  %(message)s'
    )

    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)

        color_formatter = Formatter(self.FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return


"""
    
icon = ICONS['WARN']

FORMAT = '[%(levelname)s] \033[31m%(lineno)s\033[0m:%(module)s/%(funcName)s\n\t%(message)s'
FORMAT = f' \033[35m{icon}\033[0m [%(levelname)s] \033[31m%(lineno)s\033[0m:%(module)s/%(funcName)s\n\t%(message)s'


def get_logger(logger_name, level='DEBUG'):
    logger = logging.getLogger(logger_name)
    coloredlogs.install(
        fmt=FORMAT,
        level=level,
        logger=logger)
    return logger
"""
