import logging

## logging setting

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m-%d %H:%M:%S',
handlers=[logging.FileHandler('app1.log'), logging.StreamHandler()]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a + b
    logger.info(f"Adding {a} and {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.info(f"Subtracting {a} and {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.info(f"Multiplying {a} and {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.info(f"Dividing {a} and {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"Error: {e}")
        return None
    
add(10, 20)
subtract(15, 10)
multiply(5, 5)
divide(10, 5)