import logging


class Logger:
    def get_logger(self):
        # 创建日志对象
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            sh = logging.StreamHandler()
            fmt = logging.Formatter(fmt='[%(filename)s]:%(asctime)s - %(levelname)s - %(message)s')
            sh.setFormatter(fmt)
            sh.setLevel(logging.DEBUG)
            logger.addHandler(sh)
        return logger


        # logger.info('this is info')
        # logger.warning('this is warning')
        # logger.debug('this is debug')
