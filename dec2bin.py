import sys
import argparse

def bin2dec(value, verbose):
    decimal_value = 0
    index = len(value) - 1
    for x in value:
        if verbose == 'true':
            print("{}*2**{}  ".format(x, index), end='')
        decimal_value += (int(x) * (2**(index)))
        index -= 1
    if verbose == 'true':
        print()
    return decimal_value

def dec2bin(value, verbose):
    return 3

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a binary to decimal or from decimal to binary.')
    parser.add_argument('--b2d', dest='bin2dec',  action='store_const', const=bin2dec, help='Convert the binary value to decimal')
    parser.add_argument('--d2b', dest='dec2bin',  action='store_const', const=dec2bin, help='Convert the decimal value to binary')
    parser.add_argument('--verbose', default='true', help='Print out the operation description')
    parser.add_argument('value', help='The value to convert')
    
    args = parser.parse_args()
    if args.bin2dec:
        decimal_value = args.bin2dec(args.value, args.verbose)
        print("Binary", args.value, "to Decimal is", decimal_value)
    else:
        binary_value = args.dec2bin(args.value, args.verbose)
        print("Decimal", args.value, "to Binary is", binary_value, "")