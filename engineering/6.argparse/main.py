#!/bin/python3
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="convert yaml to json", prog='main', epilog='Wait for your comments',
                                     prefix_chars="-")

    parser.add_argument('-y', '--yaml_file', metavar="/path/to/your/daemon.yaml",
                        help="path to your docker daemon config", required=True)
    parser.add_argument('-j', '--json_file')

    parser.add_argument('-v', '--validate', help="Validate your docker daemon config",
                         action="store_true")

    args = parser.parse_args()
    print(args)
    # print(args.yaml_file)



if __name__ == '__main__':
    main()