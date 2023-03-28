import argparse
import json


def start_parser():
    parser = argparse.ArgumentParser(description='A program that greets you')

    parser.add_argument('-f', '-filename', dest='path_to_file', type=str, help='File to check')
    parser.add_argument('-v', '-verbose', dest='activated_decorator', action='store_true',
                        help='Bool for activated_decorator')

    args = parser.parse_args()

    address = args.path_to_file
    activated_decorator = args.activated_decorator
    with open(address) as file:
        phone_book = json.load(file)
        return phone_book, activated_decorator


my_phone_book, verbose = start_parser()

