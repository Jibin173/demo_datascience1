import logging


class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:logging.root.removeHandler(handler)
        logging.basicConfig(filename="E://demo_datascience//Logs//test.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
