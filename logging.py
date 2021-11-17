import logging

# Logging levels:
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Create a logger instance 
# a standard naming to know where the log comes from is __name__
logger = logging.getLogger(__name__)
#set the level to DEBUG
logger.setLevel(logging.DEBUG) 

# formatter for how to display or save the text
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# the handler allow to customize multiple output for the logs
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# stream is what appears on the terminal
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# finally add the handler to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # by using exception it is possible to also get a traceback
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))