#! /usr/local/bin/python3
"""
Test of logging module
"""

import logging
logging.basicConfig(level=logging.WARNING)

def main():
    """
        Test of logging module
    """
    logging.warning('this is warning')
    logging.critical('this is critical')



if __name__ == "__main__":
    main()
