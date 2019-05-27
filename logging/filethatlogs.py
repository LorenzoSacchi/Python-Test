#! /usr/local/bin/python3

import logging
logging.basicConfig(level=logging.WARNING)

def main():
    logging.warning(f'this is warning')
    logging.critical(f'this is critical')



if __name__ == "__main__":   
    main()
