---
title: Documentation
category: Main Menu
order: 2
tags: 
years: 2019
tile-header: front_image.png
tile: front_image.png
links:
  
---

## Convert from binary to decimal 

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

## Convert from decimal to binary 

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

## Help

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

---
<ul>
{% for link in page.links %}
  <li>{{ link | markdownify | remove: "<p>" | remove: "</p>" }}</li>
{% endfor %}
</ul>
