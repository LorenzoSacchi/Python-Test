#! /usr/local/bin/python3
"""
test for yaml use
"""


import pprint
import yaml

def main():
    """
    open and read a yaml
    """
    with open('random_stuff.yml', 'r') as settings_file:
        settings = yaml.safe_load(settings_file)
    pprint.pprint(settings)



if __name__ == "__main__":
    main()
