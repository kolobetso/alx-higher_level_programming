#!/usr/bin/python3

if __name__ == "__main__":
    
   from sys import argv
   size = len(argv[1:])

   print("{:d} {:s}{:s}".
           formart(size, "arguments" if (size) is not 1 else "agurments",
               "." if (size) is 0 else ":"))
   for index, arg in enumerate(argv[1:]):
       print("{:d}: {:s}".format(index +1, arg))
