
# <p style="text-align: center;" align="center">dec2bin</p>

Convert a binary to decimal and decimal to binary (according to 'The Art of Assembly Language' Book Chapter 1).

___

## Table of content
- [Installation](#installation)
- [Method implemented from TAOA](#method-implemented-from-taoa)
	- [Binary to Decimal](#binary-to-decimal)
	- [Decimal to Binary](#decimal-to-binary)
- [Documentation](#documentation)
	- [Convert from binary to decimal](#convert-from-binary-to-decimal)
	- [Convert from decimal to binary](#convert-from-decimal-to-binary)
	- [Help](#help)
- [Contributing](#contributing)
- [License](#license)

## Installation 

You first need to download the [dec2bin.py](https://github.com/quickutils/dec2bin/blob/master/dec2bin.py) script from the repo or 
clone the complete repo [here](https://github.com/quickutils/dec2bin). 
To run the script from command line or use it in another project you need [Python](https://www.python.org/) installed on your system.

## Method implemented from TAOA

This is copied from [TAOA](https://www.amazon.com/Art-Assembly-Language-2nd/dp/1593272073) word for word.

The binary system works just like decimal numbering system with two exceptions: binary only allow the digit  0 and 1 
(rather than 0 - 9), and binary uses powers of two rather than powers of 10. Therefore, it is easy to convert a binary number 
to decimal.

### Binary to Decimal

For each "1" in the binary string, add in 2\*\*n where "n" is the zero-based position of the binary digit. For example, 
the binary value 11001010 represents:

```
1*2**7 + 1*2**6 + 0*2**5 + 0*2**4 + 1*2**3 + 0*2**2 + 1*2**1 + 0*2**0
128 + 64 + 8 + 2
202
```

### Decimal to Binary

To convert decimal to binary is slightly more difficult. You must find those powers of two which when added together 
produce the decimal result. The easiest method is to work from the a large power of two down to 2\*\*0. Consider the decimal value 1359

 1. 2\*\*10 = 1024, 2\*\*11 = 2048. So 1024 is the largest power of two less than 1359. Subtract 1024 from 1359 and begin the binary value on the left with a "1" digit. Binary = "1", Decimal result is 1359 - 1024 = 335. 
   
 2. The next lower power of two (2\*\*9 = 512) is greater than the result from above, so add a "0" to the end of the binary  string. Binary = "10", Decimal result is still 335.
   
 3. The next lower power of two is 256(2\*\*8). Substract this from 335 and add a "1" digit to the end of the binary number. Binary = "101", Decimal result is 79.
 
 4. 128 (2\*\*7) is greater than 79, so tack a "0" to the end of the binary string. Binary = "1010", Decimal result remains 79.
 
 5. The next lower power of two (2\*\*6 = 64) is less than 79, so subtract 64 and append "1" to the end of the binary string. Binary = "10101", Decimal result is 15. 
 
 6. 15 is less than the next power of two (2\*\*5 = 32) so simply add a "0" to the end of the binary string. Binary = "101010", Decimal result is still 15.

 7. 16 (2\*\*4) is greater than the remainder so far, so append a "0" to the end of the binary string. Binary = "1010100", Deciomal result is 15.  
 
 8. 2\*\*3 (eight) is less than 15, so stick another "1" digit on the end of the binary string. Binary = "10101001", Decimal result is 7.
 
 9. 2\*\*2 is less than seven, so subtract four from seven and append another one to the binary string. Binary = "101010011", decimal result is 3.
 
 10. 2\*\*1 is less than three, so append a one to the end of the binary string and subtract two from the decimal value. Binary = "1010100111", Decimal result is now 1.
 
 11. Finally, the decimal result is one, which is 2\*\*0, so add a final "1" to the end of the binary string. The final binary is "10101001111".

## Documentation

### Convert from binary to decimal 

To convert from binary to decimal the flag `--b2d` flag is used follow by the 
binary value 

```
python dec2bin.py --b2d 11001010
```

The script will convert the binary to decimal with the full description printed in the 
terminal. to prevent printing of the description the `--verbose false` should be issued 
along with the flag `--b2d`.

The commands above will print out the following result...

```
1*(2**7)  + 1*(2**6)  + 0*(2**5)  + 0*(2**4)  + 1*(2**3)  + 0*(2**2)  + 1*(2**1)  + 0*(2**0)
Binary 11001010 to Decimal is 202
```

### Convert from decimal to binary 

To convert from deciomal to binary the flag `--d2b` flag is used follow by the decimal value

```
python dec2bin.py --d2b 1359
```

The script will convert the decimal to binary with the full description printed in the 
terminal. to prevent printing of the description the `--verbose false` should be issued 
along with the flag `--d2b`.

The commands above will print out the following result...

```
1359 largest possible power of two is 10
(2**10) > 1359       hence 1359-1024     binary+=1
(2**9) > 335           hence 335-0       binary+=0
(2**8) > 335          hence 335-256      binary+=1
(2**7) > 79             hence 79-0       binary+=0
(2**6) > 79            hence 79-64       binary+=1
(2**5) > 15             hence 15-0       binary+=0
(2**4) > 15             hence 15-0       binary+=0
(2**3) > 15             hence 15-8       binary+=1
(2**2) > 7              hence 7-4        binary+=1
(2**1) > 3              hence 3-2        binary+=1
(2**0) > 1              hence 1-1        binary+=1
Decimal 1359 to Binary is 10101001111
```

### Help

To view all available command from the command line, use the `-h` command

```
dec2bin -h
```

The help screen is printed like below

```
usage: dec2bin.py [-h] [--b2d] [--d2b] [--verbose VERBOSE] value

Convert a binary to decimal or from decimal to binary.

positional arguments:
  value              The value to convert

optional arguments:
  -h, --help         show this help message and exit
  --b2d              Convert the binary value to decimal
  --d2b              Convert the decimal value to binary
  --verbose VERBOSE  Print out the operation description
```

## Contributing

Before you begin contribution please read the contribution guide at [CONTRIBUTING GUIDE](https://thedarkprojects.github.io/devjammer/contribute)

## License