---
layout: default
---

## What is dec2bin

dec2bin.py is a python script that convert a binary to decimal and decimal with detail explanation in the console. 
The method used for the conversion is scoped from [The Art of Assembly](https://www.amazon.com/Art-Assembly-Language-2nd/dp/1593272073) detailed 
explanation of binary and decimal in Chapter One. The method might not be the best approach for the conversion but it is more easy 
to grasp and understand what is really going on. **This does not cater for float point values**.

## How do i use it 

You first need to download the [dec2bin.py](https://github.com/quickutils/dec2bin/blob/master/dec2bin.py) script from the repo or 
clone the complete repo [here](https://github.com/quickutils/dec2bin). 
To run the script from command line or use it in another project you need [Python](https://www.python.org/) installed on your system.

## Method implemented from TAOA

This is copied from [TAOA](https://www.amazon.com/Art-Assembly-Language-2nd/dp/1593272073) word for word.

The binary system works just like decimal numbering system with two exceptions: binary only allow the digit  0 and 1 
(rather than 0 - 9), and binary uses powers of two rather than powers of 10. Therefore, it is easy to convert a binary number 
to decimal.

#### Binary to Decimal

For each "1" in the binary string, add in 2\*\*n where "n" is the zero-based position of the binary digit. For example, 
the binary value 11001010 represents:

```
1*2**7 + 1*2**6 + 0*2**5 + 0*2**4 + 1*2**3 + 0*2**2 + 1*2**1 + 0*2**0
128 + 64 + 8 + 2
202
```

#### Decimal to Binary

To convert decimal to binary is slightly more difficult. You must find those powers of two which when added together 
produce the decimal result. The easiest method is to work from the a large power of two down to 2\*\*0. Consider the decimal value 1359

 - 2\*\*10 = 1024, 2\*\*11 = 2048. So 1024 is the largest power of two less than 1359. Subtract 1024 from 1359 and begin the binary value on the left with a "1" digit. Binary = "1", Decimal result is 1359 - 1024 = 335. 
   
 - The next lower power of two (2\*\*9 = 512) is greater than the result from above, so add a "0" to the end of the binary  string. Binary = "10", Decimal result is still 335.
   
 - The next lower power of two is 256(2\*\*8). Substract this from 335 and add a "1" digit to the end of the binary number. Binary = "101", Decimal result is 79.
 
 - 128 (2\*\*7) is greater than 79, so tack a "0" to the end of the binary string. Binary = "1010", Decimal result remains 79.
 
 - The next lower power of two (2\*\*6 = 64) is less than 79, so subtract 64 and append "1" to the end of the binary string. Binary = "10101", Decimal result is 15. 
 
 - 15 is less than the next power of two (2\*\*5 = 32) so simply add a "0" to the end of the binary string. Binary = "101010", Decimal result is still 15.

 - 16 (2\*\*4) is greater than the remainder so far, so append a "0" to the end of the binary string. Binary = "1010100", Deciomal result is 15.  
 
 - 2\*\*3 (eight) is less than 15, so stick another "1" digit on the end of the binary string. Binary = "10101001", Decimal result is 7.
 
 - 2\*\*2 is less than seven, so subtract four from seven and append another one to the binary string. Binary = "101010011", decimal result is 3.
 
 - 2\*\*1 is less than three, so append a one to the end of the binary string and subtract two from the decimal value. Binary = "1010100111", Decimal result is now 1.
 
 - Finally, the decimal result is one, which is 2\*\*0, so add a final "1" to the end of the binary string. The final binary is "10101001111".

## Where is the code?

Yes the project is open source and the codes are [here https://github.com/quickutils/dec2bin](https://github.com/quickutils/dec2bin). 
Do not hesitate to make a contribution to the project or open an issue. 

## Licence 

The project is licenced under the [MIT Licence](https://opensource.org/licenses/MIT), which means you can uses it for whatever without 
any objectections and whatever you use it for is upto you.

## Contributors

[Thecarisma](https://www.twitter.com/iamthecarisma).

---
