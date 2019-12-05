import sys
import argparse

def bin2dec(value, verbose = 'false'):
    decimal_value = 0
    index = len(value) - 1
    for x in value:
        if verbose == 'true':
            print("{}*(2**{})  {} ".format(x, index, ( "+" if (index != 0) else "")), end='')
        decimal_value += (int(x) * (2**(index)))
        index -= 1
    if verbose == 'true':
        print()
    return decimal_value

def dec2bin(value, verbose = 'false'):
    binary_value = ""
    true_value = int(value)
    largest_power = 0
    power_result = 0
    while (2**largest_power) < true_value:
        largest_power += 1
    largest_power -= 1
    if verbose == 'true':
        print("{} largest possible power of two is {}".format(value, largest_power))
    for k in range(largest_power, -1, -1):
        power_result =  2 ** k
        if power_result > true_value:
            if verbose == 'true':
                print("{0:<18} {1:^20} {2:>10}".format('(2**{}) > {}'.format(k, true_value), 'hence {}-0'.format(true_value), 'binary+=0'))
            binary_value += "0"
        else:
            if verbose == 'true':
                print("{0:<18} {1:^20} {2:>10}".format('(2**{}) < {}'.format(k, true_value), 'hence {}-{}'.format(true_value, power_result), 'binary+=1'))
            true_value = true_value - power_result
            binary_value += "1"
    return binary_value

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