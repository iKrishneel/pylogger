#!/usr/bin/env python


from pylogger import get_logger


def test_logger():
    logger = get_logger('pylogger')

    logger.debug('Debug')
    logger.info('Info')
    logger.warning('Warning')
    logger.error("Error")

test_logger()
