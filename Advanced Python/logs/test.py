from logger import logging

def add(a, b):
    logging.debug(f'Adding {a} and {b}')
    return a + b

logging.debug('The addition function is called')
add(10, 15)