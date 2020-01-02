import os
import logging
from logging import handlers


class PluginMessageLogger(object):

    level_relations = {    # log level
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, level='info', when='D', backupCount=3,
                 fmt='%(asctime)s - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(self.get_log_path())
        format_str = logging.Formatter(fmt)  # set log format
        self.logger.setLevel(self.level_relations.get(level))  # set log level
        th = handlers.TimedRotatingFileHandler(filename=self.get_log_path(), when=when,
                                               backupCount=backupCount,
                                               encoding='utf-8')
        if not self.logger.handlers:
            th.setFormatter(format_str)
            th.setLevel(self.level_relations.get(level))
            self.logger.addHandler(th)

    @staticmethod
    def get_log_path():
        return os.path.dirname(os.path.abspath(__file__))


def get_logger():
    print("hello")
    logger = PluginMessageLogger()
    return logger


if __name__ == '__main__':
    log = get_logger()
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('warning')
    log.logger.error('error')
    log.logger.critical('critical')
    # import os
    # logging_path = os.path.dirname(os.path.abspath(__file__))
    # print(logging_path)
    # from os import path
    # logging_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
