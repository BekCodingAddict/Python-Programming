import logging

# Set up handlers explicitly
file_handler = logging.FileHandler("app.log", mode="w")
stream_handler = logging.StreamHandler()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[file_handler, stream_handler],
    force=True
)

logger = logging.getLogger("Arithmetic_Calculator")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by zero: {a}/{b}")
        return None

# Test
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
