#! /usr/local/bin/python3

import yaml
import pprint

def main():
    with open('random_stuff.yml','r') as settings_file:
        settings = yaml.safe_load(settings_file)
    pprint.pprint(settings)



if __name__ == "__main__":
    main()

    