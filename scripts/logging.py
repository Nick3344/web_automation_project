import logging

# Configure logging
logging.basicConfig(filename='logs/execution.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example of logging an info message
logging.info('This is an info message.')

# Example of logging an error message
try:
    # Code that may cause an error
    raise ValueError('This is a test error')
except ValueError as e:
    logging.error(f'An error occurred: {e}')
