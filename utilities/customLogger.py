import logging


class LogGen:
    @staticmethod
    def getLogger():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler('.\\Logs\\automation.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s",datefmt='%Y-%m-%d %H:%M:%S')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        logger.info("Logger is initialized")
        return logger
