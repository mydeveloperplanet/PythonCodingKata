# Print the value of an argument given to the main function
# Can you print the help also?
# Use argparse
import argparse


def print_text(text):
    print(text)


def main():
    parser = argparse.ArgumentParser(description='This is exercise 4.')
    parser.add_argument('text', help='The text to print')
    args = parser.parse_args()
    print_text(args.text)


if __name__ == "__main__":
    main()
