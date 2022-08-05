#Сюда можно записать все Assertions и использовать их в тестах.
import logging


class Utils:

    def assertListItemText(self, list, value):
        for stop in list:
            print("The text is: " + stop.text)
            assert stop.text == value
            print("Assertion PASSED.")

    def loggenerator(logLevel=logging.DEBUG):
        fhandler = logging.FileHandler(filename="C://PycharmProjects//Frameworks//Framework_1//logs//automation.log", mode="a")
        formatter_1 = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter_1)

        console_log_handler = logging.StreamHandler()
        formatter_2 = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        console_log_handler.setFormatter(formatter_2)



        logger = logging.getLogger()
        logger.addHandler(fhandler)
        logger.addHandler(console_log_handler)
        logger.setLevel(logLevel)
        return logger